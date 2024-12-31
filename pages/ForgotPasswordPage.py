from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.OtpPage import OtpPage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.home_routing_path = (By.XPATH, "//a[normalize-space()='Home']")
        self.title_of_forgot_password = (By.XPATH, "//p[text()='Forgot password']")
        self.email_field = (By.XPATH, "//button[.='Get Code']/preceding-sibling::div//input")
        self.get_code_button = (By.XPATH, "//button[@type='submit']")
        self.warning_message_for_email = (By.XPATH, "//div[@id='email_help']/div")

    def display_status_of_forgot_password(self):
        self.wait_for_element_visibility(self.title_of_forgot_password, 5)
        return self.is_element_displayed(self.title_of_forgot_password)

    def enter_email_address_for_otp(self, email_address_text):
        self.wait_for_element_visibility(self.email_field)
        self.write_on_element(self.email_field, email_address_text)

    def click_on_get_code_button(self):
        self.click_on_element(self.get_code_button)
        return OtpPage(self.driver)

    def retrieve_empty_email_warning_message_in_forgot_password(self):
        self.wait_for_element_visibility(self.warning_message_for_email, 3)
        return self.get_element_text(self.warning_message_for_email)


