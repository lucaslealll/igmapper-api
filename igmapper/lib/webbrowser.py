# bibliotecas
import glob
import pickle
import platform
import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings("ignore")


def start_browser(
    url: str = "https://google.com.br",
    chromedriver: str = "",
    headless: bool = False,
    soundless: bool = True,
) -> webdriver.Chrome:
    """
    Initialize a Chrome browser using Selenium.

    Parameters:
    - chromedriver_path (str): The path to the Chrome WebDriver executable.
    - url_login (str): The desired login URL.
    - headless (bool): Indicates whether to run the browser in headless mode (default: False).

    Returns:
    - browser (webdriver.Chrome): The initialized Chrome browser object.

    Usage example:
    chromedriver_path = "path/to/chromedriver"
    url_login = "https://www.example.com"
    browser = start_browser(chromedriver_path, url_login, headless=True)
    """

    OPTS = webdriver.ChromeOptions()

    if headless:
        OPTS.add_argument("--headless")
        OPTS.headless = True

    if soundless:
        OPTS.add_argument("--mute-audio")

    OPTS.add_argument("--allow-insecure-localhost")
    OPTS.add_argument("--disable-dev-shm-usage")
    OPTS.add_argument("--disable-dev-shm-using")
    OPTS.add_argument("--disable-extensions")
    OPTS.add_argument("--disable-gpu")
    OPTS.add_argument("--disable-infobars")
    OPTS.add_argument("--disable-setuid-sandbox")
    OPTS.add_argument("--disable-web-security")
    OPTS.add_argument("--ignore-certificate-errors")
    OPTS.add_argument("--no-sandbox")
    OPTS.add_argument("--remote-debugging-port=9222")
    OPTS.add_argument("--start-maximized")
    OPTS.add_argument("--window-size=1920,1080")

    system_type = platform.system()

    if system_type == "Windows" or system_type == "Darwin":
        browser = webdriver.Chrome(options=OPTS)
    elif system_type == "Linux":
        browser = webdriver.Chrome(options=OPTS, executable_path=chromedriver)
    else:
        raise OSError("Sistema operacional não identificado")

    try:
        browser.get(url)
        return browser
    except Exception as e:
        print(f"Erro ao abrir o URL: {str(e)}")
        browser.quit()


def extract_cookies(driver, directory) -> None:
    "save cookie as `cookie.pkl`"
    with open(f"{directory}/cookies.pkl", "wb") as file:
        pickle.dump(driver.get_cookies(), file)


def import_cookies(file_path, file_name, webdriver_browser):
    """Import cookies to browser.

    Parameters
    ----------
    `file_path` : Full file path.
    `file_name` : Full file_name or is prefix.
    `webdriver_browser` : Browser object

    Examples
    --------
    Implement cookie file to bypass login

    >>> importCookies("/home/computer/Desktop/", "cookieFile", driver)
    >>> importCookies("/home/computer/Desktop/", "cookieFile.pkl", driver)
    """
    try:
        for file in glob.glob(f"{file_path}*{file_name}*"):
            pwd_file = str(file)
            print(pwd_file)
    except:
        return False
    file = pickle.load(open(f"{pwd_file}", "rb"))
    for cookie in file:
        webdriver_browser.add_cookie(cookie)
    return webdriver_browser


def check_element(element_xpath: str = "") -> bool:
    """
    Function to check if an element exists on a web page based on the provided XPath.

    Args:
        element_xpath (str): XPath expression to locate the element on the web page.

    Returns:
        bool: True if the element is found, False otherwise.
    """
    try:
        browser.find_element(By.XPATH, element_xpath)
        return True
    except:
        return False


def esc_or_click(
    webdriver: webdriver, ignore_xpath: str, esc: bool = False, click_on_class: str = ""
) -> None:
    """
    Function to either press the ESC key or click on an element on a web page.

    Args:
        ignore_xpath (str): XPath expression to locate the element to ignore.
        esc (bool): If True, press the ESC key. Defaults to False.
        click_on_class (str): Class name to locate the element to click on. Defaults to an empty string.

    Returns:
        None
    """
    count = 0
    while check_element(ignore_xpath) == True and count < 3:
        if esc == True:
            # Press the ESC key
            webdriver.ActionChains(webdriver).send_keys(Keys.ESCAPE).perform()
        else:
            # Click on the element with the provided class name
            webdriver.find_element(
                By.XPATH, f"//*[contains(@class, '{click_on_class}')]"
            ).click()
