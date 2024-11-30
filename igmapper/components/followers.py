# Função para obter seguidores
from igmapper import (
    API_BASE_FRIENDSHIPS,
    API_END_FOLLOWERS,
    bold_str,
    instagram_request,
)


def get_user_followers(
    user_id: str, csrftoken: str, sessionid: str, xigappid="936619743392459"
) -> list:

    try:
        # Construir URL para buscar seguidores
        url = API_BASE_FRIENDSHIPS + user_id + API_END_FOLLOWERS

        # Cabeçalhos para requisição
        headers = {
            "cookie": f"csrftoken={csrftoken}; ds_user_id={user_id}; sessionid={sessionid}",
            "x-ig-app-id": xigappid,
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
                API_BASE_FRIENDSHIPS
                + user_id
                + f"/followers/?count=25&max_id={next_max_id}"
                if next_max_id
                else None
            )

            print(f"\rFetched followers [{len(all_followers)}]", end="", flush=True)

        # Retornar lista completa de seguidores
        print(" Done")
        return all_followers

    except Exception as e:
        # Lançar exceção com log detalhado
        print(f"{bold_str('E:')} Fetching Followers: {str(e)}")
        raise
