import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.search_page import SearchPage
import allure
from pages.cart_page import CartPage
from  pages.product_page import ProductPage
@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.automationpractice.pl/index.php")
    driver.maximize_window()
    yield driver
    driver.get("http://www.automationpractice.pl/index.php")  # Navigate back to home page after each test
    driver.quit()


@allure.feature('Login Feature')
@allure.story('Login with invalid user')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_invalid_user(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login_page()
    login_page.login("invalid@example.com", "wrongpassword")

    # Assert that the "Authentication failed" message is displayed
    assert login_page.is_error_message_displayed(), "Authentication failed message not displayed"



@allure.feature('Search Feature')
@allure.story('Search for a product')
@allure.severity(allure.severity_level.NORMAL)
def test_search(driver):
    search_page = SearchPage(driver)
    search_page.search_and_select_product("Dress")
    # Add assertions to confirm the product was selected
    time.sleep(2)
    assert "Dress" in driver.page_source, "The 'Dress' keyword should return relevant products."


@allure.feature('Add to Cart Feature')
@allure.story('Add product to the cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):
    # Initialize the required page objects
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # Add product to cart
    product_page.add_product_to_cart()

    # Verify success message item added to cart
    cart_page.wait_for_success_message()
    assert cart_page.is_success_message_displayed(), "Product successfully added message not displayed."
