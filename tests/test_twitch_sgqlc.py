import urllib.request
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from twitch_sgqlc import __version__, schema, get_client_id, DEFAULT_CLIENT_ID

import pytest


@pytest.fixture
def twitch_homepage():
    with urllib.request.urlopen("https://twitch.tv/") as f:
        yield f.read().decode()


def test_version():
    assert __version__ == "0.1.0"


def test_regex(twitch_homepage: str):
    assert get_client_id(twitch_homepage) == DEFAULT_CLIENT_ID
