import os
import platform
import subprocess
import zipfile

import requests


# Função para obter a versão do Google Chrome instalado
def get_chrome_version():
    try:
        system = platform.system()

        if system == "Windows":
            version = subprocess.check_output(
                [
                    "reg",
                    "query",
                    r"HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon",
                    "/v",
                    "version",
                ],
                encoding="utf-8",
            )
            return version.split("    ")[-1].strip()

        elif system == "Darwin":  # Para MacOS
            version = subprocess.check_output(
                [
                    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--version",
                ],
                encoding="utf-8",
            )
            return version.strip().split(" ")[-1]

        elif system == "Linux":  # Para Linux
            version = subprocess.check_output(
                ["google-chrome", "--version"], encoding="utf-8"
            )
            return version.strip().split(" ")[-1]

        else:
            print(f"Sistema operacional não suportado: {system}")
            return None
    except Exception as e:
        print(f"Erro ao obter a versão do Chrome: {e}")
        return None


# Função para baixar o chromedriver
def download_chromedriver(chrome_version):
    op_sys = platform.system()
    base_url = f"https://chromedriver.storage.googleapis.com/{chrome_version}"

    # Definindo a URL de download do chromedriver com base no sistema operacional
    if op_sys == "Windows":
        url = f"{base_url}/chromedriver_win64.zip"
    elif op_sys == "Darwin":  # MacOS
        url = f"{base_url}/chromedriver_mac64.zip"
    elif op_sys == "Linux":  # Linux
        url = f"{base_url}/chromedriver_linux64.zip"
    else:
        print(f"Sistema não suportado para download do chromedriver: {op_sys}")
        return

    # Baixar o chromedriver
    response = requests.get(url)
    if response.status_code == 200:
        zip_path = "chromedriver.zip"
        with open(zip_path, "wb") as f:
            f.write(response.content)

        # Extrair o conteúdo do ZIP
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall()

        os.remove(zip_path)  # Deletar o arquivo ZIP após extração
        print("chromedriver baixado e extraído com sucesso!")
    else:
        print("Erro ao baixar o chromedriver. Verifique a versão.")


# Função principal
def main():
    versao_chrome = get_chrome_version()
    if versao_chrome:
        print(f"Versão do Chrome instalada: {versao_chrome}")
        download_chromedriver(versao_chrome)
    else:
        print("Não foi possível determinar a versão do Chrome.")


if __name__ == "__main__":
    main()
