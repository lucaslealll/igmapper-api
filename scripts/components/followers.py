from components.instagram import BASE_URL_FRIENDSHIPS, XIGAPPID, instagram_request


def getUserFollowers(id: str, csrftoken) -> list:
    """
    Retrieves a list of followers for the specified Instagram user ID.

    Args:
        id (str): The Instagram user ID to retrieve followers for.

    Returns:
        list: A list of dictionaries containing follower information.
    """
    # Construct the URL for fetching user followers.
    url = BASE_URL_FRIENDSHIPS + id + f"/followers/?count=25"
    # Set the necessary headers, including the csrf token and user ID.
    headers = {
        "cookie": f"csrftoken={csrftoken}; ds_user_id={id}; sessionid={id}%3A8o8K5zLqGYCyet%3A1%3AAYdPySdgKgpc33bh1Xn3Q5oatRSyiKl131JhQuPZLw;",
        "x-ig-app-id": XIGAPPID,
    }
    all_followers = []
    while url:
        # Make the API request to fetch followers.
        data = instagram_request(url, headers)
        if data is None:
            # Return the followers list if there's an error.
            return all_followers

        # Extract the list of followers from the response.
        users = data.get("users", [])
        all_followers.extend(users)

        # Get the next page ID for pagination.
        next_max_id = data.get("next_max_id")
        # Update the URL for the next page of followers.
        url = (
            BASE_URL_FRIENDSHIPS + id + f"/followers/?count=25&max_id={next_max_id}"
            if next_max_id
            else None
        )

        # Print progress to the console.
        print(f"Loading...{len(all_followers)}", end="\r", flush=True)

    # Return the full list of followers.
    return all_followers
