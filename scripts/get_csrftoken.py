# %%
# ========================================================================
# == ABRE O SELENIUM E COM UMA JS INJECTION EXTRAI OS COOKIES DA PÁGINA ==
# ========================================================================
from time import sleep

from lib.web_browser.tools import start_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CHROMEDRIVER = r"/usr/local/bin/chromedriver"
COOKIE = "../src/instagram_cookies"
INJECTION = "injection/JavaScript/cookie.js"

URL = "https://instagram.com/"
XPATH_BUTTOM_ACCEPT_COOKIES = "//*[contains(text(), 'Allow all cookies')]"

# %%
driver = start_browser(
    url=URL, chromedriver=CHROMEDRIVER, headless=True, soundless=True
)

try:
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, XPATH_BUTTOM_ACCEPT_COOKIES))
    ).click()
    sleep(5)  # IMPORTANTE AGUARDAR PARA A PÁGINA GERAR TODOS PARÂMETROS
except:
    pass

# %%
js_injection = open(INJECTION, "r").read()

# Executando o script JavaScript e capturando o retorno
cookie = driver.execute_script(js_injection)
driver.quit()

open(COOKIE, "w").write(str(cookie))
