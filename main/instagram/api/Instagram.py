import requests

class Instagram:
    """
    A class to interact with Instagram's web profile info API.

    Attributes:
        username (str): Instagram username.
        csrftoken (str): CSRF token from Instagram cookies.
        ds_user_id (str): The user ID from Instagram cookies. Optional parameter.
    """

    # Application ID for Instagram API requests.
    xigappid = "936619743392459"

    def __init__(self, username: str, csrftoken: str, ds_user_id: str = ""):
        """
        Initializes the Instagram class with the provided username, csrf token, and optional user ID.

        Args:
            username (str): Instagram username.
            csrftoken (str): CSRF token from Instagram cookies.
            ds_user_id (str): Optional. Instagram user ID from cookies.
        """
        # Base URLs for Instagram API endpoints.
        self.base_url_users = "https://www.instagram.com/api/v1/users/web_profile_info/"
        self.base_url_friendships = "https://www.instagram.com/api/v1/friendships/"
        self.username = username
        self.csrftoken = csrftoken
        self.ds_user_id = ds_user_id



    def __make_request__(self, url: str, headers: dict) -> dict:
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
            print(f"An error occurred: {e}")
            return None



    def getUserProfileInfo(self) -> dict:
        """
        Retrieves the profile information for the specified Instagram username.

        Returns:
            dict: A dictionary containing the user's profile information.
        """
        # Construct the URL for fetching user profile info.
        url = self.base_url_users + "?username=" + self.username
        # Set the necessary headers, including the csrf token.
        headers = {
            "cookie": f"csrftoken={self.csrftoken}",
            "x-ig-app-id": self.xigappid,
        }
        # Make the API request and return the response.
        return self.__make_request__(url, headers)



    def getUserFollowers(self, id: str) -> list:
        """
        Retrieves a list of followers for the specified Instagram user ID.

        Args:
            id (str): The Instagram user ID to retrieve followers for.

        Returns:
            list: A list of dictionaries containing follower information.
        """
        # Construct the URL for fetching user followers.
        url = self.base_url_friendships + id + f"/followers/?count=25"
        # Set the necessary headers, including the csrf token and user ID.
        headers = { 
            "cookie": f"csrftoken={self.csrftoken}; ds_user_id={self.ds_user_id}; sessionid={self.ds_user_id}%3A8o8K5zLqGYCyet%3A1%3AAYdPySdgKgpc33bh1Xn3Q5oatRSyiKl131JhQuPZLw;",
            "x-ig-app-id": self.xigappid,
        }
        all_followers = []
        while url:
            # Make the API request to fetch followers.
            data = self.__make_request__(url, headers)
            if data is None:
                # Return the followers list if there's an error.
                return all_followers

            # Extract the list of followers from the response.
            users = data.get('users', [])
            all_followers.extend(users)
            
            # Get the next page ID for pagination.
            next_max_id = data.get("next_max_id")
            # Update the URL for the next page of followers.
            url = self.base_url_friendships + id + f"/followers/?count=25&max_id={next_max_id}" if next_max_id else None

            # Print progress to the console.
            print(f"Loading...{len(all_followers)}", end="\r", flush=True)
        
        # Return the full list of followers.
        return all_followers



    def getUserFollowing(self, id: str) -> list:
        """
        Retrieves a list of users that the specified Instagram user ID is following.

        Args:
            id (str): The Instagram user ID to retrieve the following list for.

        Returns:
            list: A list of dictionaries containing following user information.
        """
        # Construct the URL for fetching users that the specified ID is following.
        url = self.base_url_friendships + id + f"/following/?count=25"
        # Set the necessary headers, including the csrf token and user ID.
        headers = {
            'cookie': f"csrftoken={self.csrftoken}; ds_user_id={self.ds_user_id}; sessionid={self.ds_user_id}%3A8o8K5zLqGYCyet%3A1%3AAYdPySdgKgpc33bh1Xn3Q5oatRSyiKl131JhQuPZLw;",
            "x-ig-app-id": self.xigappid,
        }

        all_following = []
        while url:
            # Make the API request to fetch the list of following users.
            data = self.__make_request__(url, headers)
            if data is None:
                # Return the following list if there's an error.
                return all_following
            
            # Extract the list of following users from the response.
            users = data.get('users', [])
            all_following.extend(users)

            # Get the next page ID for pagination.
            next_max_id = data.get("next_max_id")
            # Update the URL for the next page of following users.
            url = self.base_url_friendships + id + f"/following/?count=25&max_id={next_max_id}" if next_max_id else None
            
            # Print progress to the console.
            print(f"Loading...{len(all_following)}", end="\r", flush=True)

        # Return the full list of following users.
        return all_following



    def __description__(self):
        """
        Prints the current specifications of the Instagram class instance.
        This includes the username, csrf token, user ID, and base URLs.
        """
        print(f"Instagram Class Specifications:")
        print(f"CSRF Token: {self.csrftoken}")
        print(f"DS User ID: {self.ds_user_id}")
        print(f"Username: {self.username}")
        print(f"x-ig-app-id: {self.xigappid}")
        print(f"Base URL for Friendships: {self.base_url_friendships}")
        print(f"Base URL for Users: {self.base_url_users}")
