from igmapper import API_BASE_FEED, API_END_FEED, bold_str, instagram_request


def feed(username, csrftoken, max_id, xigappid="936619743392459") -> tuple:

    url = API_BASE_FEED + username + API_END_FEED + max_id
    headers = {"cookie": f"csrftoken={csrftoken}", "x-ig-app-id": xigappid}

    try:
        response = instagram_request(url, headers)
        response_type = response.headers.get("Content-Type", "").split(";")[0]
        response_status_code = response.status_code
        return response, response_type, response_status_code
    except Exception as e:
        print(f"{bold_str('E:')}", str(e))
        raise
