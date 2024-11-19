# %%
import os
import pickle
from time import sleep

from components import (
    bold,
    getUserFollowers,
    getUserFollowing,
    getUserProfileInfo,
    italic,
)
from lib import start_browser, extract_cookies

# Define paths for source and logs
CWD = os.getcwd()  # current working directory
SRC, LOG = f"{CWD}/src", f"{CWD}/logs"
PKL = f"{SRC}/cookies.pkl"

CHROMEDRIVER = f"{CWD}/scripts/chromedriver"
URL = "https://instagram.com/"
XPATH_CONTAINER_FEED = "//*[contains(@class, 'xw7yly9')]"

# %%
print(f"{bold('Instagram Followers & Unfollowers')}\n")

usr = input(bold("Enter the Instagram username (without '@'): "))
if not usr:
    print("No username provided. Exiting.")
    exit(1)

# %%
try:
    cookie = pickle.load(open(PKL, "rb"))
    print("Cookie file founded...")
except:
    print(f"{bold('Login • Instagram')}\n{italic('You need to login to continue')}")

    driver = start_browser(
        url=URL, chromedriver=CHROMEDRIVER, headless=False, soundless=True
    )

    sleep(60)

    extract_cookies(driver, SRC)

cookie = pickle.load(open(PKL, "rb"))
for i in cookie:
    if "csrftoken" in i["name"]:
        csrftoken = i["value"]
    if "sessionid" in i["name"]:
        sessionid = i["value"]

# Retrieve user account information
print("Retrieving user account ID...")
acc = getUserProfileInfo(usr, csrftoken)

# If the account information could not be retrieved, exit the program
if not acc:
    print("Failed to retrieve account information. Exiting.")
    exit(1)
else:
    # Save account profile information to a JSON log file
    open(f"{LOG}/{usr}-profile_info.json", "w").write(str(acc))

    # Extract user ID from the fetched account data
    user = acc["data"]["user"]
    user_id = user["id"]
    # print(f"User profile ID fetched successfully!")


bio = user["biography"]
bio_links = user["bio_links"]
category_name = user["category_name"]
follow = user["edge_follow"]["count"]
followed = user["edge_followed_by"]["count"]
full_name = user["full_name"]
is_private = user["is_private"]
is_verified = user["is_verified"]
posts_count = user["edge_owner_to_timeline_media"]["count"]

# {italic(f'https://www.instagram.com/{usr}')}
output = f"""{bold('Investigated profile:')}
－ {usr} {"🟓" if is_verified else ""}
－ {bold(posts_count)} posts     {bold(followed)} followers     {bold(follow)} following
－ {full_name if full_name else "No name"}
－ {italic(category_name) if category_name else "No category"}
－ "{bio if bio else "No bio"}"
－ {f'{[i["url"] for i in bio_links]}' if bio_links else "No links"}
－ {bold('This account is private') if is_private else "Public account"}"""
print(output)


# Retrieve the user's followers and following lists using the user ID
try:
    print("Get followers...")
    acc_followers = getUserFollowers(user_id, csrftoken, sessionid)
    print("Get following...")
    acc_following = getUserFollowing(user_id, csrftoken, sessionid)
except Exception as e:
    exit()

# Create dictionaries to store 'following' and 'followers' details
following_dict, followers_dict = {}, {}

# Populate the 'following' dictionary with usernames and full names
print("Building following dictionary...")
for i in acc_following:
    usr = i.get("username")
    following_dict[usr] = i.get("full_name")

# Populate the 'followers' dictionary with usernames and full names
print("Building followers dictionary...")
for i in acc_followers:
    usr = i.get("username")
    followers_dict[usr] = i.get("full_name")

# Find users that are in 'following' but not in 'followers' (people who don't follow back)
print("Get non followers...")
non_followers = [i for i in following_dict if i not in followers_dict]

# Print usernames that the user follows but who don't follow back
_ = (
    input(bold("Do you want to show the don't follow back list? [Y/n]: "))
    .strip()
    .lower()
)
if _ == "" or _ == "y":
    print(bold("Don't follow back:"))
    if non_followers:
        for i, usr in enumerate(sorted(non_followers), 1):
            fullname = following_dict[usr]
            print(f"  {i}) {fullname:<30} {usr:<30} {URL+usr}")
    else:
        print("None - Everyone you follow also follows you back!")

# Print the full list of 'following'
_ = input(bold("Do you want to show the following list? [Y/n]: ")).strip().lower()
if _ == "" or _ == "y":
    for i, usr in enumerate(acc_following, 1):
        username, fullname = usr["username"], usr["full_name"]
        print(f"  {i}) {fullname:<30} {username:<30} {URL+username}")

_ = input(bold("Do you want to show the followers list? [Y/n]: ")).strip().lower()
if _ == "" or _ == "y":
    for i, usr in enumerate(acc_followers, 1):
        username, fullname = usr["username"], usr["full_name"]
        print(f"  {i}) {fullname:<30} {username:<30} {URL+username}")
