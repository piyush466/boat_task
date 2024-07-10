import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1950,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.boat-lifestyle.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.save_screenshot("../Screenshot/after.png")
    yield driver
    driver.quit()


# Add custom environment info
from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    config.stash[metadata_key]["TESTER"] = "PIYUSH"
    config.stash[metadata_key]["PROJECT"] = "BOAT"

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
