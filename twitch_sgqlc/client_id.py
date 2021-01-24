import re

CLIENT_ID_REGEX = r"\"Client-ID\":\"(?P<client_id>.*)\",\"Content-Type\""
def get_client_id(text: str) -> str:
    """Extract the Client-ID from Twitch's homepage. You probably don't need this, as it seems that Twitch has a universal ID: ``

    Args:
        text (str): HTML from Twitch's homepage

    Returns:
        str: The Client-Id, will be empty if not found.
    """
    
    match = re.match(CLIENT_ID_REGEX, text)
    return match.group("client_id") if match else ""
