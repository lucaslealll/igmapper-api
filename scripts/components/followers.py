from components.instagram import BASE_URL_FRIENDSHIPS, XIGAPPID, instagram_request
from components.utils import bold


# Função para obter seguidores
def getUserFollowers(user_id: str, csrftoken: str, sessionid: str) -> list:

    try:
        # Construir URL para buscar seguidores
        url = BASE_URL_FRIENDSHIPS + user_id + "/followers/?count=25"

        # Cabeçalhos para requisição
        headers = {
            "cookie": f"csrftoken={csrftoken}; ds_user_id={user_id}; sessionid={sessionid}",
            "x-ig-app-id": XIGAPPID,
        }

        all_followers = []

        while url:
            # Fazer requisição à API
            data = instagram_request(url, headers)
            if "error" in data:
                # Retornar seguidores acumulados se houver erro
                print(data["details"])  # Log de erro
                return all_followers

            # Extrair lista de seguidores da resposta
            users = data.get("users", [])
            all_followers.extend(users)

            # Pegar o ID da próxima página para paginação
            next_max_id = data.get("next_max_id")
            url = (
                BASE_URL_FRIENDSHIPS
                + user_id
                + f"/followers/?count=25&max_id={next_max_id}"
                if next_max_id
                else None
            )

        # Retornar lista completa de seguidores
        return all_followers

    except Exception as e:
        # Lançar exceção com log detalhado
        print(f"{bold('E:')} Fetching Followers: {str(e)}")
        raise
