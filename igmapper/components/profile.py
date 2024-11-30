from igmapper import API_BASE_USERS, instagram_request


def get_user_profile_info(username, csrftoken, xigappid="936619743392459") -> dict:
    """
    Retrieves the profile information for the specified Instagram username.

    Returns:
        dict: A dictionary containing the user's profile information.
    """
    # Construct the URL for fetching user profile info.
    url = API_BASE_USERS + username
    # Set the necessary headers, including the csrf token.
    headers = {"cookie": f"csrftoken={csrftoken}", "x-ig-app-id": xigappid}
    # Make the API request and return the response.
    return instagram_request(url, headers)
