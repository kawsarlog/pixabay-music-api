"""GET /v1/search. Change the values below, then run it.

Run from the repo folder:
    python examples/search.py
"""

import client

QUERY = "cinematic"
PAGE = 1
ORDER = "latest"  # relevant, latest, editors_choice
GENRE = ""
MOOD = ""
MOVEMENT = ""
THEME = ""
DURATION = "30-120"  # 0-30, 30-120, 120-240, 240-480
CONTENT = "human"  # all, human, ai

data = client.get(
    "/v1/search",
    {
        "q": QUERY,
        "page": PAGE,
        "order": ORDER,
        "genre": GENRE,
        "mood": MOOD,
        "movement": MOVEMENT,
        "theme": THEME,
        "duration": DURATION,
        "content": CONTENT,
    },
)

print(data["total"], "tracks, page", data["page"], "of", data["pages"])
for track in data["tracks"]:
    stats = track["stats"]
    print(
        f"{track['id']:>8}  {track['duration']:>7}  "
        f"views {stats['views']:<6}  {track['name']}"
    )
