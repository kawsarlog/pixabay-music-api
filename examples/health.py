"""GET /health. Prints {"ok": true} when the API is up.

Run from the repo folder:
    python examples/health.py
"""

import client

client.show(client.get("/health"))
