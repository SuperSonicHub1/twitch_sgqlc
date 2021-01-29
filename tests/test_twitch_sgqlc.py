import urllib.request
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from twitch_sgqlc import __version__, schema, get_client_id, DEFAULT_CLIENT_ID

import pytest


@pytest.fixture
def twitch_homepage():
    with urllib.request.urlopen("https://twitch.tv/") as f:
        yield f.read().decode()

@pytest.fixture
def endpoint():
    yield HTTPEndpoint(
    "https://gql.twitch.tv/gql",
    base_headers={"Client-ID": DEFAULT_CLIENT_ID},
)


def test_version():
    assert __version__ == "0.1.0"


def test_regex(twitch_homepage: str):
    assert get_client_id(twitch_homepage) == DEFAULT_CLIENT_ID


def test_schema(endpoint: HTTPEndpoint):
    # Get a user's login
    op = Operation(schema.Query)
    op.user(login="monstercat").login()
    data = endpoint(op)

    user: schema.Query.user = (op + data).user
    
    assert user.login == "monstercat"



