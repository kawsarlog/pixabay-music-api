"""GET /v1/discover. Prints the catalog size and a few search ideas.

Run from the repo folder:
    python examples/discover.py
"""

import client

data = client.get("/v1/discover")
print("catalog", data.get("catalog_total"))
print("popular searches:")
for item in data.get("popular_searches") or []:
    print(" ", item.get("name"), item.get("search_path"))
print("themes:")
for item in (data.get("themes") or [])[:8]:
    print(" ", item.get("name"), item.get("search_path"))
print("featured", len(data.get("featured_tracks") or []))
