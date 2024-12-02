from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[1]/a")  # Sign in button
        self.username_field = (By.XPATH, "//*[@id='email']")  # Email input field
        self.password_field = (By.ID, "passwd")  # Password input field
        self.submit_button = (By.ID, "SubmitLogin")  # Submit button
        self.error_message = (By.XPATH, "//*[contains(text(), 'Authentication failed')]")  # Error message XPath

    def navigate_to_login_page(self):
        # Wait for the "Sign in" button to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_button)
        )
        self.driver.find_element(*self.sign_in_button).click()

    def enter_username(self, username):
        # Wait for the email field to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        )
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        # Wait for the password field to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        )
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_submit(self):
        # Wait for the submit button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        self.driver.find_element(*self.submit_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

    def is_error_message_displayed(self):
        # Check if the error message "Authentication failed" is displayed
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_message)
            )
            return True
        except:
            return False