from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.PharmacySelectionPage import PharmacySelectionPage


class LogInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title_of_login_page = (By.XPATH, "//h4")
        self.owner_radio_button = (By.XPATH, "//input[@value='Owner']")
        self.pharmacist_radio_button = (By.XPATH, "//input[@value='Pharmacist']")
        self.email_address_field = (By.XPATH, "//input[@id='login_username']")
        self.phone_number_field = (By.XPATH, "//input[@id='login_primaryPhone']")
        self.password_field = (By.XPATH, "//input[@id='login_password']")
        self.eye_button_on_password = (By.XPATH, "//i[@aria-label='icon: eye-invisible']")
        self.eye_invisible_on_password = (By.XPATH, "//*[@data-icon='eye-invisible']")
        self.eye_visible_on_password = (By.XPATH, "//*[@data-icon='eye']")
        self.log_in_button = (By.XPATH, "//button[@type='submit']")
        self.warning_message_for_email = (By.XPATH, "//input[@id='login_username']/ancestor::span/following-sibling::div")
        self.warning_message_for_password = (By.XPATH, "//input[@id='login_password']/ancestor::span/following-sibling::div")
        self.warning_message_for_phone = (By.XPATH, "//input[@id='login_primaryPhone']/ancestor::span/following-sibling::div")
        self.warning_message_for_api = (By.XPATH, "//span[@class='ant-alert-message']")

    def navigate_to_base_page(self, context):
        self.navigate_to_base_url(context.base_url)

    def display_status_of_log_in_page(self):
        element = self.wait_for_element_visibility(self.title_of_login_page)
        return element.is_displayed()
        # return self.is_element_displayed(self.title_of_login_page)

    def click_on_owner_radio_button(self):
        status_selected = self.is_element_selected(self.owner_radio_button)
        if status_selected:
            pass
        else:
            self.click_on_element(self.owner_radio_button)

    def click_on_pharmacist_radio_button(self):
        status_selected = self.is_element_selected(self.pharmacist_radio_button)
        if status_selected:
            pass
        else:
            self.click_on_element(self.pharmacist_radio_button)

    def enter_email_address(self, email_address_text):
        self.write_on_element(self.email_address_field, email_address_text)

    def enter_password(self, password_text):
        self.write_on_element(self.password_field, password_text)

    def click_on_log_in_button(self):
        self.click_on_element(self.log_in_button)
        return PharmacySelectionPage(self.driver)

    def click_on_eye_button(self):
        self.click_on_element(self.eye_button_on_password)

    def retrieve_password_visibility(self):
        return self.get_attribute_value(self.password_field, "value")

    def retrieve_email_warning_message(self):
        element = self.wait_for_element_visibility(self.warning_message_for_email, 3)
        return element.text

    def retrieve_password_warning_message(self):
        element = self.wait_for_element_visibility(self.warning_message_for_password, 3)
        return element.text

    def retrieve_phone_warning_message(self):
        element = self.wait_for_element_visibility(self.warning_message_for_phone, 3)
        return element.text

    def retrieve_incorrect_email_or_password_warning_message(self):
        element = self.wait_for_element_visibility(self.warning_message_for_api, 3)
        return element.text

    def display_status_of_eye_invisible(self):
        return self.is_element_displayed(self.eye_invisible_on_password)

    def display_status_of_eye_visible(self):
        return self.is_element_displayed(self.eye_visible_on_password)
