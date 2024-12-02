from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "search_query_top")  # Update locator for the search box
        self.search_button = (By.NAME, "submit_search")  # Update locator for the search button
        self.no_product_message = (By.CSS_SELECTOR, ".alert-warning")  # Locator for "No products available" message
        self.add_to_cart_button = (By.CSS_SELECTOR, ".ajax_add_to_cart_button")  # Update locator for Add to Cart button

    def search_for_product(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    def is_no_product_available_message_displayed(self):
        try:
            return self.driver.find_element(*self.no_product_message).is_displayed()
        except:
            return False

    def try_add_to_cart(self):
        try:
            # Try clicking the Add to Cart button
            self.driver.find_element(*self.add_to_cart_button).click()
        except:
            pass  # Handle scenario where add to cart fails due to no products

    def is_add_to_cart_button_disabled(self):
        try:
            button = self.driver.find_element(*self.add_to_cart_button)
            return 'disabled' in button.get_attribute('class')  # Check if the button is disabled
        except:
            return False