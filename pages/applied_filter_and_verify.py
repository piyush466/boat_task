from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Boat_e2e:

    click_on_category_xpath = "//span[text()='Categories']"
    select_earbuds_xpath = "//p[text()='True Wireless Earbuds']"
    click_on_filter_xpath = "//button[text()='Filter By']"
    select_price_filter_xpath = "//button[text()='Price']"
    select_from_price_id = "filter.v.price.gte"
    select_to_price_id = "filter.v.price.lte"
    click_apply_btn_css = "[class='button button--primary button--full']"
    click_on_playback_xpath = "//button[text()='Playback']"
    select_payback_filter_css = "input[value='50-75 Hrs']"
    product_value_css = "[class='price price--highlight product-card-price']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def click_on_category(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_category_xpath))).click()


    def selecting_the_earbuds(self):
        self.wait.until((EC.element_to_be_clickable((By.XPATH, self.select_earbuds_xpath)))).click()


    def click_on_filter(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_filter_xpath))).click()


    def select_filter(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.select_price_filter_xpath))).click()

    def enter_the_price(self,from_price,to_price):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.select_from_price_id))).send_keys(from_price)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.select_to_price_id))).send_keys(to_price)

    def click_on_apply_filter(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.click_apply_btn_css))).click()

    def refresh_page(self):
        self.driver.refresh()

    def click_on_payback(self):
        self.script = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_playback_xpath)))
        self.driver.execute_script("arguments[0].click();", self.script)

    def select_the_payback_filter_value(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_payback_filter_css))).click()















