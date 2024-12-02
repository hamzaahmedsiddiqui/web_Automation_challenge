from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.ID, "search_query_top")
        self.search_button = (By.NAME, "submit_search")
        self.first_product = (By.XPATH, "//ul[@class='product_list grid row']//li[1]")

    def enter_search_query(self, query):
        self.driver.find_element(*self.search_field).send_keys(query)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def select_first_product(self):
        self.driver.find_element(*self.first_product).click()

    def search_and_select_product(self, query):
        self.enter_search_query(query)
        self.click_search_button()
        self.select_first_product()