from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.success_message_text = "Product successfully added to your shopping cart"
        self.cart_button_title = "View my shopping cart"
        self.product_name = "Printed Summer Dress"

    def wait_for_success_message(self, timeout=2):
        # Wait for the success message to be visible
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))

    def is_success_message_displayed(self):
        # Check if the success message contains the expected text
        success_message = self.driver.find_element(By.TAG_NAME, "h2")
        return success_message.is_displayed() and self.success_message_text in success_message.text

    def go_to_cart(self):
        # Click on the cart button using the title
        cart_button = self.driver.find_element(By.XPATH, f"//a[@title='{self.cart_button_title}']")
        cart_button.click()

    def is_product_in_cart(self):
        # Verify that the product is in the cart by checking the product's name
        cart_product = self.driver.find_element(By.XPATH, f"//a[@title='{self.product_name}']")
        return cart_product.is_displayed()