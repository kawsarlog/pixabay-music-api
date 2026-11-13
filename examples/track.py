"""GET /v1/tracks/{id}. Change TRACK_ID, then run it.

Run from the repo folder:
    python examples/track.py
"""

import client

TRACK_ID = 632729

data = client.get(f"/v1/tracks/{TRACK_ID}")
track = data["track"]
client.show(
    {
        "id": track["id"],
        "name": track["name"],
        "duration": track["duration"],
        "published_at": track.get("published_at"),
        "genres": track.get("genres"),
        "moods": track.get("moods"),
        "attribution": track["attribution"],
        "page_url": track["page_url"],
        "audio_url": track["audio_url"],
        "youtube_content_id": track["youtube_content_id"],
        "is_ai_generated": track["is_ai_generated"],
        "stats": track["stats"],
        "file": track.get("file"),
        "related": [item["id"] for item in data["related"]],
    }
)
