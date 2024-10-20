# %%
# ========================================================================
# == ABRE O SELENIUM E COM UMA JS INJECTION EXTRAI OS COOKIES DA PÁGINA ==
# ========================================================================
from time import sleep

from lib.web_browser.tools import start_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

JS_CODE_COOKIE = "injections/JavaScript/cookie.js"

CHMDVR = r"../src/chromedriver"
URL = "https://instagram.com/"
XPATH_BUTTOM_ACCEPT_COOKIES = "//*[contains(text(), 'Allow all cookies')]"

# %%
driver = start_browser(url=URL, chromedriver_path=CHMDVR, headless=True, soundless=True)

try:
    print(
        "Allow the use of cookies from Instagram on this browser? [Allow all cookies]",
        end="",
    )
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, XPATH_BUTTOM_ACCEPT_COOKIES))
    ).click()
    sleep(5)  # IMPORTANTE AGUARDAR PARA A PÁGINA GERAR TODOS PARÂMETROS
    print("✅")
except:
    print("❌")
    pass

# %%
with open(JS_CODE_COOKIE, "r") as f:
    js_code_cookie = f.read()

# Executando o script JavaScript e capturando o retorno
cookie = driver.execute_script(js_code_cookie)
driver.quit()

with open("../src/instagram_cookies", "w") as f:
    f.write(str(cookie))
