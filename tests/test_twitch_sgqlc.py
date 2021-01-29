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
    op = Operation(schema.Query)
    
    user = op.user(login="monstercat")
    # Get a user's login
    user.login()
    # See when a user started a stream
    user.stream().created_at()
    data = endpoint(op)

    query: schema.Query = (op + data)
    
    assert query.user.login == "monstercat"
    assert query.user.stream.created_at



