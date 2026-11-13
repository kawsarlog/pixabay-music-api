"""Shared caller for the example scripts. No extra packages."""

import json
import sys
import urllib.parse
import urllib.request

API = "https://92g9yktme1.execute-api.us-east-1.amazonaws.com/prod"
KEY = "dA5Wd0nQe08lvUDeiudst6CSjMPTpeqr1nNAsfOD"


def get(path, params=None):
    url = API + path
    if params:
        query = {key: value for key, value in params.items() if value not in (None, "")}
        if query:
            url += "?" + urllib.parse.urlencode(query)
    request = urllib.request.Request(url, headers={"x-api-key": KEY})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def open_url(url, headers):
    """Return status, headers, and body. Does not follow redirects."""

    class NoRedirect(urllib.request.HTTPErrorProcessor):
        def http_response(self, request, response):
            return response

        https_response = http_response

    opener = urllib.request.build_opener(NoRedirect)
    request = urllib.request.Request(url, headers=headers)
    with opener.open(request, timeout=60) as response:
        return response.status, response.headers, response.read()


def show(data):
    text = json.dumps(data, indent=2, ensure_ascii=False)
    sys.stdout.buffer.write(text.encode("utf-8", errors="replace") + b"\n")
