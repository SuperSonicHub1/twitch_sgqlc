import re

DEFAULT_CLIENT_ID = "kimne78kx3ncx6brgo4mv6wki5h1ko"
CLIENT_ID_REGEX = r"\"Client-ID\":\"(?P<client_id>.*)\",\"Content-Type\""


def get_client_id(text: str) -> str:
    """Extract the Client-ID from Twitch's homepage. You probably don't need this, as it seems that Twitch has a universal ID: `kimne78kx3ncx6brgo4mv6wki5h1ko`

    Args:
        text (str): HTML from Twitch's homepage

    Returns:
        str: The Client-Id, will be empty if not found.
    """

    match = re.search(CLIENT_ID_REGEX, text)
    return match.group("client_id") if match else ""
