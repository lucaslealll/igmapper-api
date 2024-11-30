import urllib


from igmapper import API_BASE_COMMENTS, API_END_COMMENTS, instagram_request


def get_comments(
    media_id, cookie, next_min_id=None, xigappid="936619743392459"
) -> tuple:
    csrftoken = cookie["csrftoken"]
    ds_user_id = cookie["ds_user_id"]
    sessionid = cookie["sessionid"]

    url = API_BASE_COMMENTS + media_id + API_END_COMMENTS

    if next_min_id:
        url += f"?min_id={next_min_id}"

    headers = {
        "cookie": f"csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid};",
        "x-ig-app-id": xigappid,
    }

    response = instagram_request(url, headers)
    response_type = response.headers.get("Content-Type", "").split(";")[0]
    response_status_code = response.status_code

    next_min_id = response.json().get("next_min_id")
    next_min_id = urllib.parse.quote(next_min_id) if next_min_id else None

    return response, next_min_id, response_type, response_status_code
