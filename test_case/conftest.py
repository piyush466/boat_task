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
<<<<<<< HEAD
    driver = webdriver.Chrome()
    driver.get("https://www.boat-lifestyle.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.save_screenshot("/Screenshot/after.png")
=======
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.boat-lifestyle.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.save_screenshot("screenshots/after.png")
>>>>>>> 5e1838bc564bffc9ba2891793e143ac1f3a2e023

    yield driver
    driver.quit()