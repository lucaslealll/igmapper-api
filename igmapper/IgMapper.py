import os

from igmapper import web_profile_info

CWD = os.getcwd()  # current working directory
SRC, LOG = f"{CWD}/src", f"{CWD}/logs"
PKL = f"{SRC}/cookies.pkl"


class Instagram:
    def __init__(self, auth, username):
        self.auth = auth
        self.username = username

    

    def getUserProfileInfo():
        acc = web_profile_info(usr, csrftoken)
        user = acc["data"]["user"]
        user_id = user["id"]

    def __str__(self):
        return f"Username: {self.username}"
