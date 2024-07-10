import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.logging_file import LogGen
from pages.applied_filter_and_verify import Boat_e2e


class Test_product_filter:
    product_price_value_css = "[class='price price--highlight product-card-price']"


    def test_e_2_e_flow(self, setup):
        self.driver = setup
        self.logs = LogGen.logger()
        self.wait = WebDriverWait(self.driver, 10)
        self.boat = Boat_e2e(self.driver)
        self.boat.click_on_category()
        self.driver.implicitly_wait(10)
        self.boat.selecting_the_earbuds()
        self.boat.click_on_filter()
        self.boat.select_filter()
        self.boat.enter_the_price("500", "1000")
        self.boat.click_on_apply_filter()
        self.driver.execute_script("window.scrollTo(400,0)")
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.boat.click_on_filter()
        self.boat.click_on_payback()
        self.boat.select_the_payback_filter_value()
        self.price_product = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.product_price_value_css))).text
        self.convert_to_int = int(self.price_product[-3:])
        self.logs.info("********Assertion Started***********")
        assert 500 <= self.convert_to_int <= 1000, "Assertion is not match"



    def test_title_of_page(self, setup):
        self.driver = setup
        self.logs = LogGen.logger()
        self.logs.info("******CHECKING THE TITLE OF PAGE*******")
        self.title = self.driver.title
        assert self.title == "Buy Earbuds, Headphones, Earphones at India’s No.1 Earwear Brand: boAt", "TTILE IS NOT MATCH"










