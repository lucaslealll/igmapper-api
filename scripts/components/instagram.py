import requests

# Application ID for Instagram API requests.
XIGAPPID = "936619743392459"
BASE_URL_USERS = "https://www.instagram.com/api/v1/users/web_profile_info/"
BASE_URL_FRIENDSHIPS = "https://www.instagram.com/api/v1/friendships/"


def instagram_request(url: str, headers: dict) -> dict:
    """
    Makes an HTTP GET request to the specified URL with the given headers.

    Args:
        url (str): The URL to send the request to.
        headers (dict): The headers to include in the request.

    Returns:
        dict: The JSON response from the request, or None if an error occurred.
    """
    try:
        # Send the GET request to the specified URL.
        response = requests.get(url, headers=headers, timeout=5)
        # Raise an exception for HTTP errors.
        response.raise_for_status()
        # Return the JSON response as a dictionary.
        return response.json()
    except requests.exceptions.RequestException as e:
        # Print the error if the request fails.
        print(e)
        return None
