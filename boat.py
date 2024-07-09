import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.boat-lifestyle.com/")
driver.implicitly_wait(10)
driver.maximize_window()
wait = WebDriverWait(driver,10)

driver.find_element(By.XPATH, "//span[text()='Categories']").click()
driver.find_element(By.XPATH, "//p[text()='True Wireless Earbuds']").click()

driver.find_element(By.XPATH, "//button[text()='Filter By']").click()

wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Price']"))).click()
time.sleep(2)
# driver.find_element(By.XPATH, "//button[text()='Price']").click()
driver.find_element(By.ID, "filter.v.price.gte").send_keys("500")
driver.find_element(By.ID, "filter.v.price.lte").send_keys("1000")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='button button--primary button--full']"))).click()
driver.refresh()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Filter By']").click()

exicute = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Playback']")))

driver.execute_script("arguments[0].click();", exicute)
# driver.find_element(By.XPATH, "//button[text()='Playback']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[value='50-75 Hrs']").click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='button button--primary button--full']"))).click()
time.sleep(3)
value_of_product = driver.find_element(By.CSS_SELECTOR, "[class='price price--highlight product-card-price']")
convert_to_int = int(value_of_product.text[-3:])

assert  500 <= convert_to_int <= 1000, "not match"







