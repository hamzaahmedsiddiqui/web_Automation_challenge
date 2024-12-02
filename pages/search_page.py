from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.ID, "search_query_top")
        self.search_button = (By.NAME, "submit_search")
        self.first_product = (By.XPATH, "//ul[@class='product_list grid row']//li[1]")  # First product in the list by XPATH

    def enter_search_query(self, query):
        # Enter the search query
        self.driver.find_element(*self.search_field).send_keys(query)

    def click_search_button(self):
        # Click the search button
        self.driver.find_element(*self.search_button).click()

    def select_first_product(self):
        # Select the first product from the search results
        self.driver.find_element(*self.first_product).click()

    def search_and_select_product(self, query):
        self.enter_search_query(query)  # Enter the search term
        self.click_search_button()  # Click to search
        self.select_first_product()  # Select the first product from the results