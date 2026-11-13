"""GET /. Prints the route list.

Run from the repo folder:
    python examples/home.py
"""

import client

client.show(client.get("/"))
