from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

URL = "https://orteil.dashnet.org/experiments/cookie/"
CLICKABLE = "rgba(238, 238, 238, 1)"


def try_buy_upgrade():
    """
    If an element is clickable, click on it
    Throw exception if the element is stale
    :return:
    """

    try:
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div")

        for item in store[::-1]:
            if item.value_of_css_property("background-color") == CLICKABLE:
                item.click()
                break
    except StaleElementReferenceException:
        pass


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

num_cookies = driver.find_element(By.ID, value="money")
cookie = driver.find_element(By.ID, value="cookie")

while True:
    cookie.click()
    try_buy_upgrade()
