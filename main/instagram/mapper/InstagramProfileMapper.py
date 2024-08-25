# %%
from api.Instagram import Instagram
from models.InstagramProfile import InstagramProfile

class InstagramProfileMapper:
    def __init__(self, api: Instagram):
        self.api = api

    def map_profile(self, user_id: str) -> InstagramProfile:
        """Monta o perfil completo do usuário usando dados obtidos pela API."""
        profile_data = self.api.get_user_profile(user_id)
        media_data = self.api.get_user_media(user_id)
        
        return Instagram(
            id=profile_data["id"],
            username=profile_data["username"],
            media_count=profile_data["media_count"],
            media=media_data
        )

# %%
profile = InstagramProfileMapper()

# %%
user = "tutti_q"
# user = "lucas.oal"
csrftoken = "4CsiolqsKtMa88jqyqRq8Tc3KsGH0NG8"
instagram = Instagram(user, csrftoken)

# %%
acc = instagram.getUserProfileInfo()
acc_id = acc.get("data").get("user").get("id")
# acc_id = "27600439191"
acc_id

# %%
acc_followers = instagram.getUserFollowers(acc_id)

# %%
acc_following = instagram.getUserFollowing(acc_id)

# %%
# Criar dicionários para 'following' e 'followers'
following_dict = {}
followers_dict = {}

# Preencher o dicionário de 'following'
for p in acc_following:
    username = p.get("username")
    following_dict[username] = p.get("full_name")

# Preencher o dicionário de 'followers'
for p in acc_followers:
    username = p.get("username")
    followers_dict[username] = p.get("full_name")

# Encontrar usernames que estão em 'following' mas não em 'followers'
non_followers = [username for username in following_dict if username not in followers_dict]

# Imprimir os resultados
print("Usernames em 'following' mas não em 'followers':")
for i, username in enumerate(sorted(non_followers), 1):
    full_name = following_dict[username]
    print(f"Hit{i}: {full_name} [{username}]")


# %%
for i, p in enumerate(acc_following):
    arroba = p.get("username")
    nome = p.get("full_name")
    print(f"Hit{i+1}: {nome} [{arroba}]")

# %%
for i, p in enumerate(acc_followers):
    arroba = p.get("username")
    nome = p.get("full_name")
    print(f"Hit{i+1}: {nome} [{arroba}]")


