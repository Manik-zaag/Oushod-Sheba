from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage


class PharmacySelectionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title_of_pms_pharmacy_page = (By.XPATH, "//h3")
        self.get_pharmacies = (By.XPATH, "//h4")
        self.pharmacy_button_relative_xpath = (By.XPATH, "./parent::div/parent::div/following-sibling::div/button")
        self.pharmacy_address_relative_xpath = (By.XPATH, "./following-sibling::div")

    def get_pharmacy_name(self, pharmacy_name):
        pharmacy_locators = self.get_elements(self.get_pharmacies)
        for pharmacy in pharmacy_locators:
            if pharmacy.text.strip() == pharmacy_name:
                return pharmacy  # return pharmacy locator
        return None  # Return None if no matching pharmacy is found

    def display_status_of_pms_pharmacy(self):
        element = self.wait_for_element_visibility(self.title_of_pms_pharmacy_page, 5)
        return element.is_displayed()

    def retrieve_pharmacy_address(self, pharmacy_name):
        pharmacy_element = self.get_pharmacy_name(pharmacy_name)
        if pharmacy_element:
            pharmacy_address = self.get_element(self.pharmacy_address_relative_xpath, parent_element=pharmacy_element)
            return pharmacy_address.text.strip()
        else:
            raise Exception(f"Pharmacy with name '{pharmacy_name}' not found! with address")

    def select_pharmacy_button(self, pharmacy_name):
        pharmacy_element = self.get_pharmacy_name(pharmacy_name)
        if pharmacy_element:
            button = self.get_element(self.pharmacy_button_relative_xpath, parent_element=pharmacy_element)
            button.click()
            return DashboardPage(self.driver)
        else:
            raise Exception(f"Pharmacy with name '{pharmacy_name}' not found!")
