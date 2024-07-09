import pytest
from selenium import webdriver



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.boat-lifestyle.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
