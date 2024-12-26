import os
import pickle
from datetime import datetime as dtm

from igmapper import bold_str, extract_cookies, italic_str, start_browser
from igmapper.components.utils import progress_bar

CWD = os.getcwd()  # current working directory

CHROMEDRIVER = f"{CWD}/chromedriver"

SRC, LOG = f"{CWD}/src", f"{CWD}/logs"
PKL = f"{SRC}/cookies.pkl"

URL, XPATH_CONTAINER_FEED = "https://instagram.com/", "//*[contains(@class, 'xw7yly9')]"


def authorize() -> None:
    "- Get a valid cookie to extraction"
    cookie_valid, retry = False, 1

    while cookie_valid == False and retry <= 3:
        retry += 1
        try:
            cookie = pickle.load(open(PKL, "rb"))
            print("Cookie file founded...")

            for i in cookie:
                if "csrftoken" in i["name"]:
                    csrftoken = i["value"]
                if "sessionid" in i["name"]:
                    sessionid, expiry = i["value"], i["expiry"]

            expiry, now = dtm.fromtimestamp(expiry), dtm.now()
            if now > expiry:
                raise
            cookie_valid = True
        except:
            print(
                f"{bold_str('Login • Instagram')}\n{italic_str('You need to login to continue')}"
            )
            driver = start_browser(URL, CHROMEDRIVER, False, True)
            progress_bar(60)
            extract_cookies(driver, SRC)

    return str(PKL)
