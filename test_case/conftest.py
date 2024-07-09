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
    driver.save_screenshot("after.png")

    yield driver
    driver.quit()