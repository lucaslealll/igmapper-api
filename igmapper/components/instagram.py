import requests

from igmapper import bold_str

# Application ID for Instagram API requests.
API_BASE_USERS = "https://www.instagram.com/api/v1/users/web_profile_info/?username="

API_BASE_FRIENDSHIPS, API_END_FOLLOWERS, API_END_FOLLOWING = (
    "https://www.instagram.com/api/v1/friendships/",
    "/followers/?count=25",
    "/following/?count=25",
)

API_BASE_FEED, API_END_FEED = (
    "https://www.instagram.com/api/v1/feed/user/",
    "/username/?count=33&max_id=",
)
API_BASE_COMMENTS, API_END_COMMENTS = (
    "https://www.instagram.com/api/v1/media/",
    "/comments/",
)


def instagram_request(url: str, headers: dict = None) -> dict:
    """
    Makes an HTTP GET request to the specified URL with the given headers.

    Args:
        url (str): The URL to send the request to.
        headers (dict, optional): The headers to include in the request. Defaults to None.

    Returns:
        dict: The JSON response from the request, or a dictionary with error details if an error occurred.
    """
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse and return the JSON response
    except Exception as e:
        print(f"{bold_str('E:')}", str(e))
        raise
