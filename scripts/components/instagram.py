import requests
from requests.exceptions import HTTPError, RequestException
from components.utils import bold

# Application ID for Instagram API requests.
XIGAPPID = "936619743392459"
BASE_URL_USERS = "https://www.instagram.com/api/v1/users/web_profile_info/"
BASE_URL_FRIENDSHIPS = "https://www.instagram.com/api/v1/friendships/"


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
        print(f"{bold("E:")}", str(e))
        raise
