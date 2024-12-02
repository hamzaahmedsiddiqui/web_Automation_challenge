from selenium.webdriver.common.by import By
import time

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_url = "http://www.automationpractice.pl/index.php?id_product=5&controller=product&search_query=dress&results=7#/16-color-yellow/3-size-l"
        self.add_to_cart_button_xpath = "//button[@name='Submit']"

    def add_product_to_cart(self):
        self.driver.get(self.product_url)
        add_to_cart_button = self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath)
        add_to_cart_button.click()
        time.sleep(2)