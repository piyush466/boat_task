import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.logging_file import LogGen


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
        self.logs = LogGen.logger()

    def click_on_category(self):
        time.sleep(4)
        try:
            self.iframe = self.wait.until(EC.visibility_of_element_located((By.ID, "ctIframe")))
            self.driver.switch_to.frame(self.iframe)
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='wzrk-confirm']"))).click()
        except Exception as E:
           print("Exception:- ", E)
        self.driver.switch_to.default_content()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_category_xpath))).click()
        self.logs.info("********Click on the category************")


    def selecting_the_earbuds(self):
        self.driver.save_screenshot("../Screenshot/product3.png")
        self.wait.until((EC.element_to_be_clickable((By.XPATH, self.select_earbuds_xpath)))).click()
        self.logs.info("********selecting_the_earbuds************")



    def click_on_filter(self):
        self.filter = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_filter_xpath)))
        self.driver.execute_script("arguments[0].click();", self.filter)
        self.logs.info("********click_on_filter************")


    def select_filter(self):
        time.sleep(2)
        self.element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.select_price_filter_xpath)))
        self.driver.execute_script("arguments[0].click();", self.element)
        self.logs.info("********select_filter************")

    def enter_the_price(self,from_price,to_price):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.select_from_price_id))).send_keys(from_price)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.select_to_price_id))).send_keys(to_price)
        self.logs.info("********enter_the_price************")

    def click_on_apply_filter(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.click_apply_btn_css))).click()
        self.logs.info("********click_on_apply_filter************")

    def refresh_page(self):
        self.driver.refresh()

    def click_on_payback(self):
        self.script = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_on_playback_xpath)))
        self.driver.execute_script("arguments[0].click();", self.script)
        self.logs.info("********click_on_payback************")

    def select_the_payback_filter_value(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_payback_filter_css))).click()
        self.logs.info("********select_the_payback_filter_value************")
















