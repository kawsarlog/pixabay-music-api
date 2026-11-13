"""GET /v1/tracks/{id}/download. Follows the redirect and saves the MP3.

The file lands in downloads/, which is not part of the repo.
Change TRACK_ID, then run from the repo folder:
    python examples/download.py
"""

from pathlib import Path

import client

TRACK_ID = 632729

status, headers, _body = client.open_url(
    client.API + f"/v1/tracks/{TRACK_ID}/download",
    {"x-api-key": client.KEY},
)
audio_url = headers.get("Location")
if status not in (301, 302, 303, 307, 308) or not audio_url:
    raise SystemExit(f"expected a redirect to the MP3, got {status}")

# The CDN file does not need the API key. It does reject Python's default agent.
_status, file_headers, mp3 = client.open_url(
    audio_url,
    {"User-Agent": "pixabay-music-api-example"},
)
folder = Path("downloads")
folder.mkdir(exist_ok=True)
name = audio_url.rstrip("/").rsplit("/", 1)[-1] or f"{TRACK_ID}.mp3"
if not name.endswith(".mp3"):
    name = f"{TRACK_ID}.mp3"
path = folder / name
path.write_bytes(mp3)

print("redirect", status, audio_url)
print("saved", path, len(mp3), "bytes")
print("content-type", file_headers.get("Content-Type"))
print("starts with", mp3[:4])
