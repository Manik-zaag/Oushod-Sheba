from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.pharmacy_name = (By.XPATH, "//header/span/small")

    def retrieve_pharmacy_name(self):
        element = self.wait_for_element_visibility(self.pharmacy_name, 5)
        return element.text.strip()