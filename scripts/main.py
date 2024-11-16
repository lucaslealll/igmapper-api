from datetime import datetime

from components import bold, getUserFollowers, getUserProfileInfo, italic
from lib import start_browser

# Define paths for source and logs
PATH_SRC, PATH_LOG = "../src", "../logs"

output = f"""{"="*43}
{"="*2}   {bold("Instagram Followers & Unfollowers")}   {"="*2}
{"="*43}"""
print(output)

usr = input(bold("Enter the Instagram username (without '@'): "))
usr = "bellatormma"
if not usr:
    print("No username provided. Exiting.")
    exit(1)

print(f"{bold("Login • Instagram")}\n{italic("You nedd to login to continue")}")
exit()





# Read CSRF token from file to authenticate Instagram requests
csrftoken = eval(open(f"{PATH_SRC}/instagram_cookies", "r").read()).get("csrftoken")


# Retrieve user account information
print("Retrieving user account ID...")
acc = getUserProfileInfo(usr, csrftoken)

# If the account information could not be retrieved, exit the program
if not acc:
    print("Failed to retrieve account information. Exiting.")
    exit(1)
else:
    # Save account profile information to a JSON log file
    open(f"{PATH_LOG}/{usr}-profile_info.json", "w").write(str(acc))

    # Extract user ID from the fetched account data
    user = acc["data"]["user"]
    user_id = user["id"]
    print(italic(user_id))
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

output = f"""
{italic(f"https://www.instagram.com/{usr}")}
{bold(usr)} {"🟓" if is_verified else ""}
{bold(posts_count)} posts     {bold(followed)} followers     {bold(follow)} following
{bold(full_name) if full_name else "No name"}
{italic(category_name) if category_name else "No category"}
{bio if bio else "No bio"}
{bold(f"🔗 {[i["url"] for i in bio_links]}") if bio_links else "No links"}
{bold("🔒 This account is private") if is_private else ""}"""
print(output)


# Retrieve the user's followers and following lists using the user ID
print("Fetching followers and following lists...")
try:
    acc_followers = getUserFollowers(user_id, csrftoken)
    print("⤷ Followers data retrieved successfully!")
    # acc_following = getUserFollowing(user_id, csrftoken)
    # print("⤷ Following data retrieved successfully!")
except Exception as e:
    exit()

# Create dictionaries to store 'following' and 'followers' details
# following_dict, followers_dict = {}, {}

# # Populate the 'following' dictionary with usernames and full names
# print("Building following dictionary...")
# for i in acc_following:
#     usr = i.get("username")
#     following_dict[usr] = i.get("full_name")

# # Populate the 'followers' dictionary with usernames and full names
# print("Building followers dictionary...")
# for i in acc_followers:
#     usr = i.get("username")
#     followers_dict[usr] = i.get("full_name")

# # Find users that are in 'following' but not in 'followers' (people who don't follow back)
# non_followers = [
#     username for username in following_dict if username not in followers_dict
# ]

# # Print usernames that the user follows but who don't follow back
# print("\nList of users you follow but who don't follow you back:")
# if non_followers:
#     for i, usr in enumerate(sorted(non_followers), 1):
#         _full_name = following_dict[usr]
#         print(f"#{i}: {_full_name} (@{usr})")
# else:
#     print("None - Everyone you follow also follows you back!")

# # Print the full list of 'following'
# print("\nFull list of users you're following:")
# for i, usr in enumerate(acc_following, 1):
#     _username = usr.get("username")
#     _full_name = usr.get("full_name")
#     print(f"#{i}: {_full_name} (@{_username})")

# # Print the full list of 'followers'
# print("\nFull list of your followers:")
# for i, usr in enumerate(acc_followers, 1):
#     _username = usr.get("username")
#     _full_name = usr.get("full_name")
#     print(f"#{i}: {_full_name} (@{_username})")


# # Create dictionaries to store 'following' and 'followers' details
# following_dict, followers_dict = {}, {}

# # Populate the 'following' dictionary with usernames and full names
# print("Building following dictionary...")
# for i in acc_following:
#     usr = i.get("username")
#     following_dict[usr] = i.get("full_name")

# # Populate the 'followers' dictionary with usernames and full names
# print("Building followers dictionary...")
# for i in acc_followers:
#     usr = i.get("username")
#     followers_dict[usr] = i.get("full_name")

# # Find users that are in 'following' but not in 'followers' (people who don't follow back)
# non_followers = [
#     username for username in following_dict if username not in followers_dict
# ]

# # Print usernames that the user follows but who don't follow back
# print("\nList of users you follow but who don't follow you back:")
# if non_followers:
#     for i, usr in enumerate(sorted(non_followers), 1):
#         _full_name = following_dict[usr]
#         print(f"#{i}: {_full_name} (@{usr})")
# else:
#     print("None - Everyone you follow also follows you back!")

# # Print the full list of 'following'
# print("\nFull list of users you're following:")
# for i, usr in enumerate(acc_following, 1):
#     _username = usr.get("username")
#     _full_name = usr.get("full_name")
#     print(f"#{i}: {_full_name} (@{_username})")

# # Print the full list of 'followers'
# print("\nFull list of your followers:")
# for i, usr in enumerate(acc_followers, 1):
#     _username = usr.get("username")
#     _full_name = usr.get("full_name")
#     print(f"#{i}: {_full_name} (@{_username})")


# # Saída formatada
# output = f"""
# {bold(user_data['nome_usuario'])}
# {bold(user_data['quantidade_posts'])} posts     {bold(followers)} followers     {bold(following)} following 
# 🔗 {user_data['url_perfil']}

# {dont_follow_back} Don't follow you back!

# Don't followed back by: {', '.join(dfb_list) if dfb_list else 'Nenhum'}
# Followers: {', '.join(user_data['seguidores'])}
# Following: {', '.join(user_data['seguindo'])}
# """
