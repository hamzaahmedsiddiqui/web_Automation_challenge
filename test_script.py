import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
import allure
from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def driver():
    # Initialize the ChromeDriver using webdriver_manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://www.automationpractice.pl/index.php")
    driver.maximize_window()
    yield driver  # This allows the tests to use the driver, and it will quit after the test
    driver.quit()


@allure.feature('Login Feature')
@allure.story('Login with invalid user')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_invalid_user(driver):
    login_page = LoginPage(driver)
    # Navigate to the login page by clicking the Sign in button
    login_page.navigate_to_login_page()

    # Attempt login with invalid credentials
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
    assert "Dress" in driver.page_source

@allure.feature('Add to Cart Feature')
@allure.story('Attempt to add product to cart when no products are available')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):
    cart_page = CartPage(driver)
    cart_page.add_product_and_checkout()
    # Add assertions to confirm the product was added to the cart
    time.sleep(2)
    assert "Shopping-cart" in driver.page_source



