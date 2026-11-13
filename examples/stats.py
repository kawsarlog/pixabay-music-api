"""GET /v1/tracks/{id}/stats. Change TRACK_ID, then run it.

Run from the repo folder:
    python examples/stats.py
"""

import client

TRACK_ID = 632729

client.show(client.get(f"/v1/tracks/{TRACK_ID}/stats"))
