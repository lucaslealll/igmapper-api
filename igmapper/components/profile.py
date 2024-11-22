from components.instagram import BASE_URL_USERS, XIGAPPID, instagram_request


def getUserProfileInfo(username, csrftoken) -> dict:
    """
    Retrieves the profile information for the specified Instagram username.

    Returns:
        dict: A dictionary containing the user's profile information.
    """
    # Construct the URL for fetching user profile info.
    url = BASE_URL_USERS + "?username=" + username
    # Set the necessary headers, including the csrf token.
    headers = {"cookie": f"csrftoken={csrftoken}", "x-ig-app-id": XIGAPPID}
    # Make the API request and return the response.
    return instagram_request(url, headers)
