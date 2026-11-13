<p align="center">
  <img src="https://images.bigibyte.com/projects/banner.webp" width="100%" alt="Pixabay music API. Unofficial. Search tracks, read the counts, get the MP3.">
</p>

<p align="center">
  <a href="https://github.com/kawsarlog/pixabay-music-api/stargazers"><img src="https://img.shields.io/github/stars/kawsarlog/pixabay-music-api?style=social" alt="GitHub stars"></a>
  <a href="https://pixabay.com/service/license-summary/"><img src="https://img.shields.io/badge/music-Pixabay%20Content%20License-2ea44f?style=flat-square" alt="Pixabay Content License"></a>
  <a href="#limits"><img src="https://img.shields.io/badge/quota-1000%20%2F%20day-555?style=flat-square" alt="1000 requests per day"></a>
  <a href="https://www.linkedin.com/in/kawsarlog"><img src="https://img.shields.io/badge/LinkedIn-kawsarlog-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

<p align="center">
  <a href="#call-it">Call it</a> ·
  <a href="#endpoints">Endpoints</a> ·
  <a href="#search">Search</a> ·
  <a href="#a-track">A track</a> ·
  <a href="#examples">Examples</a> ·
  <a href="#try-the-files">Example files</a> ·
  <a href="#prompts">Prompts</a> ·
  <a href="#contact">Contact</a> ·
  <a href="#license">License</a>
</p>

<table>
  <tr>
    <td align="center" width="33%">
      <img src="https://images.bigibyte.com/projects/search.webp" width="220" alt="Three cream lines and a green dot">
      <br><br>
      Search<br>
      <sub>20 tracks a page. Genre, mood, and length.</sub>
    </td>
    <td align="center" width="33%">
      <img src="https://images.bigibyte.com/projects/stats.webp" width="220" alt="Four bars, the tallest one green">
      <br><br>
      Counts<br>
      <sub>Views, downloads, likes, comments, rating.</sub>
    </td>
    <td align="center" width="33%">
      <img src="https://images.bigibyte.com/projects/file.webp" width="220" alt="A file card with a green waveform inside">
      <br><br>
      The file<br>
      <sub>The MP3 link on cdn.pixabay.com.</sub>
    </td>
  </tr>
</table>

Unofficial API for the free music on [Pixabay](https://pixabay.com/music/). This project is not affiliated with Pixabay, and Pixabay does not run it. The songs are not mine. Rights stay with the artists and with Pixabay. Read the [Pixabay Content License](https://pixabay.com/service/license-summary/) before you publish a video. Free to use, including commercial work. You still can't sell the file by itself or upload their catalog to another stock site.

Author: [kawsarlog](https://github.com/kawsarlog) · [LinkedIn](https://www.linkedin.com/in/kawsarlog) · [pixabay-music-api@bigibyte.com](mailto:pixabay-music-api@bigibyte.com)

If this saved you from clicking through Pixabay for half an hour, [star the repo](https://github.com/kawsarlog/pixabay-music-api) ⭐. That's how the next person finds it.

## Call it

| | |
| --- | --- |
| Base URL | `https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod` |
| Header | `x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD` |
| Key | Public, so you can try it. Everyone on this key shares 1,000 requests a day. No Pixabay account. |
| Audio | `audio_url` is the MP3 on `cdn.pixabay.com`. This API does not host the file. |

A missing or wrong key returns `403`. When the shared day is used up you get `429`.

The key on this page is for trying the API. If you need your own 1,000 a day, email [pixabay-music-api@bigibyte.com](mailto:pixabay-music-api@bigibyte.com).

`GET /v1/tracks/{id}/download` only redirects to the same CDN file. Download `audio_url` if you want the bytes directly.

```text
GET /v1/search   →   GET /v1/tracks/{id}   →   audio_url
```

## Limits

| Limit | Value |
| --- | --- |
| Requests | 1,000 per day on a key. The public key is shared. |
| Speed | 2 per second, with a short burst of 5 |
| Page size | 20 tracks. You can't change it. |
| Duration filter | `0-30`, `30-120`, `120-240`, `240-480` seconds. Anything else is `422`. |

## Endpoints

| Method | Path | What you get |
| --- | --- | --- |
| `GET` | `/health` | `{"ok": true}` if the API is up |
| `GET` | `/` | A short list of the routes |
| `GET` | `/v1/search` | 20 tracks per page |
| `GET` | `/v1/tracks/{id}` | One track, plus related tracks |
| `GET` | `/v1/tracks/{id}/stats` | Live counts for that track |
| `GET` | `/v1/tracks/{id}/download` | Redirect to the MP3 |
| `GET` | `/v1/discover` | Catalog size, popular searches, themes |

## Search

`GET /v1/search`

| Param | What to send |
| --- | --- |
| `q` | Words, up to 100 characters. Leave it off to browse. |
| `page` | Starts at 1. |
| `order` | `relevant` (default), `latest`, or `editors_choice` |
| `genre` | A Pixabay genre name, such as `ambient` or `cinematic` |
| `mood` | Such as `relaxing` or `dark` |
| `movement` | `slow` or `fast` |
| `theme` | Such as `background music` or `vlog music` |
| `duration` | Only `0-30`, `30-120`, `120-240`, or `240-480` |
| `content` | `all`, `human`, or `ai` |

`content=human` is the one to use when the video is going to YouTube and you want tracks Pixabay has not marked as AI.

Genre, mood, movement, and theme can be combined with `q`. They use Pixabay's own names. `GET /v1/discover` lists popular searches and themes if you need ideas.

A search row does not include a trustworthy publish date. The same request time is stamped on every row. Use `GET /v1/tracks/{id}` and read `published_at`.

### What comes back

| Field | Meaning |
| --- | --- |
| `total` | How many tracks match, not just this page |
| `page` | The page you asked for |
| `per_page` | Always 20 |
| `pages` | How many pages `total` fills |
| `tracks` | The 20 tracks on this page |

## A track

Search rows and `GET /v1/tracks/{id}` share these fields. The detail call also fills genres, moods, the file size, `published_at`, and `related`.

| Field | Meaning |
| --- | --- |
| `id` | Numeric id. This is what the other routes use. |
| `name` | Title |
| `duration_seconds` | Length in seconds |
| `duration` | Same length, already formatted |
| `audio_url` | The MP3. Host is `cdn.pixabay.com`. |
| `page_url` | The track page on Pixabay. Keep this with the file. |
| `attribution` | A line like `Music by {username} from Pixabay`. Keep this too. |
| `youtube_content_id` | `true` means the track is in YouTube Content ID. A video that uses it can still get a claim. |
| `is_ai_generated` | `true` when Pixabay has marked the track as AI |
| `editors_choice` | Pixabay's editors picked it |
| `stats.views` | Views |
| `stats.downloads` | Downloads |
| `stats.likes` | Likes |
| `stats.comments` | Comments |
| `stats.collections` | Times it was saved to a collection |
| `stats.rating` | Pixabay's rating |
| `artist.username` | Public username |
| `artist.profile_url` | Artist page |
| `genres`, `moods`, `movements`, `themes` | On the detail call |
| `published_at` | On the detail call. Don't trust dates from search. |
| `file.filename` | Suggested save name |
| `file.size_label` | Size as Pixabay prints it, such as `2.1 MB` |
| `related` | Other tracks, on the detail call only |

`GET /v1/tracks/{id}/stats` is the same counts, fetched again. Use it when you need a fresh number and don't want the whole track.

`GET /v1/discover` returns `catalog_total`, `popular_searches`, `themes`, and `featured_tracks`. Each search or theme has a `search_path` you can call. There is no playlists field.

## Errors

| Status | Code | What happened |
| --- | --- | --- |
| `403` | | Missing or wrong `x-api-key` |
| `404` | `not_found` | That id is not a music track |
| `422` | `invalid_duration` | `duration` was not one of the four buckets |
| `429` | | Daily quota is gone, or you are calling too fast |
| `502` | | Pixabay did not answer. Retry once, then stop. Don't make up a track. |

```json
{"error": {"code": "invalid_duration", "message": "duration must be 0-30, 30-120, 120-240, or 240-480."}}
```

## Examples

Search for human cinematic tracks between 30 and 120 seconds, newest first:

```bash
curl -H "x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD" \
  "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod/v1/search?q=cinematic&duration=30-120&content=human&order=latest"
```

<details>
<summary>One track, the counts, and the file</summary>

```bash
curl -H "x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD" \
  "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod/v1/tracks/632729"
```

```bash
curl -H "x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD" \
  "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod/v1/tracks/632729/stats"
```

```bash
curl -L -H "x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD" \
  -o track.mp3 \
  "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod/v1/tracks/632729/download"
```

</details>

<details>
<summary>Python</summary>

```python
import json
import urllib.request

API = "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod"
KEY = "dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD"

def get(path):
    request = urllib.request.Request(API + path, headers={"x-api-key": KEY})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)

tracks = get("/v1/search?q=piano&mood=relaxing&duration=30-120&content=human")
print(tracks["total"], "tracks")
print(tracks["tracks"][0]["name"], tracks["tracks"][0]["audio_url"])
```

</details>

<details>
<summary>JavaScript</summary>

Node, Deno, or Bun. A browser page on another site cannot call this API.

```javascript
const API = "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod";
const KEY = "dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD";

const params = new URLSearchParams({
  q: "piano",
  mood: "relaxing",
  duration: "30-120",
  content: "human",
});

const response = await fetch(`${API}/v1/search?${params}`, {
  headers: { "x-api-key": KEY },
});
if (!response.ok) {
  throw new Error(`${response.status} ${await response.text()}`);
}
const tracks = await response.json();
console.log(tracks.total, "tracks");
console.log(tracks.tracks[0].name, tracks.tracks[0].audio_url);
```

</details>

## Try the files

One Python file per endpoint, plus a JavaScript search, in [examples](examples). No extra packages. The address and key for Python are in `examples/client.py`. The JavaScript file keeps its own copy. Run these from the repo folder:

| File | Endpoint |
| --- | --- |
| `node examples/search.js` | `GET /v1/search` |
| `python examples/health.py` | `GET /health` |
| `python examples/home.py` | `GET /` |
| `python examples/search.py` | `GET /v1/search` |
| `python examples/track.py` | `GET /v1/tracks/{id}` |
| `python examples/stats.py` | `GET /v1/tracks/{id}/stats` |
| `python examples/download.py` | `GET /v1/tracks/{id}/download` |
| `python examples/discover.py` | `GET /v1/discover` |

Search, track, stats, and download have a query or a track id at the top of the file. Change that, then run it again. `download.py` saves the MP3 into `downloads/`.

## Prompts

Paste one of these into Claude, Codex, or Cursor. The agent should call the HTTP API. It should not open a browser.

<details>
<summary>Pick a track</summary>

```text
Use the Pixabay music API. Do not open a browser.

Base URL: https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod
Header on every request: x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD

I need one royalty-free track for a 60 second YouTube video about cooking.
Search GET /v1/search?q=cooking&duration=30-120&content=human&order=relevant
Skip any track where youtube_content_id is true.
Open GET /v1/tracks/{id} for the best match.
Then tell me the name, id, duration, genres, attribution, page_url, stats, and audio_url.
audio_url is the MP3. Download that file. Do not use any pixabay.com/music/download/ link.
Keep the attribution with the file. Music stays under the Pixabay Content License: https://pixabay.com/service/license-summary/
If the API returns 429 or 502, retry once. If it fails again, stop and say so.
```

</details>

<details>
<summary>Match a mood and a length</summary>

```text
Use the Pixabay music API. No browser.

Base URL: https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod
Header: x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD

Find 5 calm ambient tracks between 2 and 4 minutes.
GET /v1/search?q=ambient&mood=relaxing&duration=120-240&content=human
Duration is in seconds and only these values work: 0-30, 30-120, 120-240, 240-480.
Return a table with id, name, duration, views, downloads, likes, youtube_content_id, and audio_url.
Do not download yet. I will pick one.
```

</details>

<details>
<summary>Details, counts, then the file</summary>

```text
Use the Pixabay music API. No browser.

Base URL: https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod
Header: x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD

For track 632729:
1. GET /v1/tracks/632729
2. GET /v1/tracks/632729/stats
3. Download the MP3 from audio_url (or follow GET /v1/tracks/632729/download, which redirects to the same CDN file).
Save it using the filename from the track. Quote the attribution and page_url in your reply.
The stats you report must be the views, downloads, likes, comments, and rating from the API, not a guess.
```

</details>

<details>
<summary>Let the agent choose the search</summary>

```text
You can search free music with this API. No browser, no Pixabay account.

GET https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod/v1/search
Header: x-api-key: dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD

Query params: q, page, order (relevant, latest, editors_choice), genre, mood, movement, theme, duration (0-30, 30-120, 120-240, 240-480), content (all, human, ai).
Each page returns 20 tracks. total tells you how many exist.
A track you might keep has id, name, duration_seconds, audio_url, page_url, attribution, youtube_content_id, and stats (views, downloads, likes, comments, rating).
Full record: GET /v1/tracks/{id}
Live counts: GET /v1/tracks/{id}/stats
Catalog ideas: GET /v1/discover
The MP3 is audio_url on cdn.pixabay.com.

Task: pick background music for the project I describe next. Prefer content=human and youtube_content_id false. Show me 3 options with links before you download my choice.
```

</details>

## Support

I pay for the hosting. A star helps people find this.

| | |
| --- | --- |
| Star | https://github.com/kawsarlog/pixabay-music-api |
| Site | https://kawsarlog.com |

## Contact

| | |
| --- | --- |
| LinkedIn | https://www.linkedin.com/in/kawsarlog |
| Email | [pixabay-music-api@bigibyte.com](mailto:pixabay-music-api@bigibyte.com) |

## License

All rights to the music stay with Pixabay and the artists.

[Pixabay Content License](https://pixabay.com/service/license-summary/)

## Star history

[![Star history](https://api.star-history.com/svg?repos=kawsarlog/pixabay-music-api&type=Date)](https://www.star-history.com/#kawsarlog/pixabay-music-api&Date)
