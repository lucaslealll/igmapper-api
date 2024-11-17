# %%
# ========================================================================
# == ABRE O SELENIUM E COM UMA JS INJECTION EXTRAI OS COOKIES DA PÁGINA ==
# ========================================================================
from time import sleep

from lib.webbrowser import start_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CHROMEDRIVER = r"/usr/local/bin/chromedriver"
COOKIE = "../src/instagram_cookies"
INJECTION = "injection/JavaScript/cookie.js"

URL = "https://instagram.com/"
XPATH_BUTTOM_ACCEPT_COOKIES = "//*[contains(text(), 'Allow all cookies')]"
XPATH_CONTAINER_FEED = "//*[contains(@class, 'xw7yly9')]"

# %%
driver = start_browser(
    url=URL, chromedriver=CHROMEDRIVER, headless=False, soundless=True
)

# try:
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH, XPATH_BUTTOM_ACCEPT_COOKIES))
#     ).click()
#     sleep(5)  # IMPORTANTE AGUARDAR PARA A PÁGINA GERAR TODOS PARÂMETROS
# except:
#     pass

attempts = 0
while attempts < 2:
    attempts += 1
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, XPATH_CONTAINER_FEED))
        )
        break
    except:
        print(f"Fail to login!")
        raise
# %%
js_injection = open(INJECTION, "r").read()

# Executando o script JavaScript e capturando o retorno
cookie = driver.execute_script(js_injection)
driver.quit()

open(COOKIE, "w").write(str(cookie))
