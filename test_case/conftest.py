import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    option = Options()
    option.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.get("https://www.boat-lifestyle.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
