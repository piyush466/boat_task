import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.boat-lifestyle.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()