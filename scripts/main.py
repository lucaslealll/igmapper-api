from components.followers import getUserFollowers
from components.following import getUserFollowing
from components.profile import getUserProfileInfo

# Define paths for source and logs
PATH_SRC = "../src"
PATH_LOG = "../logs"

# Read CSRF token from file to authenticate Instagram requests
with open(f"{PATH_SRC}/instagram_cookies", "r") as f:
    csrftoken = eval(f.read()).get("csrftoken")

usr = input("Enter the Instagram username (without '@'):\n⤷ ").strip()
if not usr:
    print("No username provided. Exiting.")
    exit(1)


# Retrieve user account information
print("Retrieving user account ID...")
acc = getUserProfileInfo(usr, csrftoken)

# If the account information could not be retrieved, exit the program
if not acc:
    print("Failed to retrieve account information. Exiting.")
    exit(1)
else:
    # Save account profile information to a JSON log file
    with open(f"{PATH_LOG}/{usr}-profile_info.json", "w") as f:
        f.write(str(acc))

    # Extract user ID from the fetched account data
    user_id = acc.get("data").get("user").get("id")
    print(
        f"⤷ User profile fetched successfully!\n⤷ Username: '{usr}' | User ID: '{user_id}'"
    )

# Retrieve the user's followers and following lists using the user ID
print("Fetching followers and following lists...")
acc_followers = getUserFollowers(user_id, csrftoken)
acc_following = getUserFollowing(user_id, csrftoken)

if acc_followers == [] or acc_following == []:
    print("❌ Fail to request data about followers/following")
    exit(1)

print("Data retrieved successfully!")

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
non_followers = [
    username for username in following_dict if username not in followers_dict
]

# Print usernames that the user follows but who don't follow back
print("\nList of users you follow but who don't follow you back:")
if non_followers:
    for i, usr in enumerate(sorted(non_followers), 1):
        _full_name = following_dict[usr]
        print(f"#{i}: {_full_name} (@{usr})")
else:
    print("None - Everyone you follow also follows you back!")

# Print the full list of 'following'
print("\nFull list of users you're following:")
for i, usr in enumerate(acc_following, 1):
    _username = usr.get("username")
    _full_name = usr.get("full_name")
    print(f"#{i}: {_full_name} (@{_username})")

# Print the full list of 'followers'
print("\nFull list of your followers:")
for i, usr in enumerate(acc_followers, 1):
    _username = usr.get("username")
    _full_name = usr.get("full_name")
    print(f"#{i}: {_full_name} (@{_username})")
