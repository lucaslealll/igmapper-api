import re
import requests

def getxigappid(url, csrftoken):
    """
    Realiza uma solicitação GET para a URL fornecida, utilizando um token CSRF específico no cabeçalho de cookies.
    Extrai o valor de 'X-IG-App-ID' que está presente no texto da resposta.

    Args:
    - url (str): A URL para a qual a solicitação GET será feita.
    - csrftoken (str): O token CSRF que será incluído no cabeçalho de cookies.

    Returns:
    - str: O valor de 'X-IG-App-ID' encontrado no texto da resposta, ou None se não encontrado.
    """
    headers = {"Cookie": f"csrftoken={csrftoken}"}
    response = requests.request("GET", url, headers=headers, data={})

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Procura pelo valor de X-IG-App-ID no texto da resposta usando expressão regular
        pattern = r'"X-IG-App-ID":"([^"]+)"'
        match = re.search(pattern, response.text)

        if match:
            return match.group(1)  # Retorna o valor capturado dentro dos parênteses da expressão regular
        else:
            print(f"Valor de 'X-IG-App-ID' não encontrado no texto da resposta.")
            return None
    else:
        print(f"A solicitação GET para {url} falhou. Status code: {response.status_code}")
        return None