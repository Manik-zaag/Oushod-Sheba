from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from icecream import ic

from pages.BasePage import BasePage


class OtpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.home_routing_path = (By.XPATH, "//a[normalize-space()='Home']")
        self.title_of_forgot_otp = (By.XPATH, "//p[text()='Email Verification']")
        self.email_text_field = (By.XPATH, "//p[.='Please verify your email address']/following-sibling::p")
        self.resend_code_field = (By.XPATH, "//button[.='Resend Code']")
        self.otp_fields = (By.XPATH, "//input[starts-with(@aria-label, 'Please enter OTP character')]")
        self.change_email_field = (By.XPATH, "//p[.='Change Email']")
        self.timer_field = (By.XPATH, "//div[@class='ant-statistic-content']")
        self.verify_email_field = (By.XPATH, "//span[.='Verify Email']/parent::button")

    def display_status_of_forgot_otp(self):
        try:
            self.wait_for_element_visibility(self.title_of_forgot_otp, 5)
            return self.is_element_displayed(self.title_of_forgot_otp)
        except NoSuchElementException:
            raise Exception("Otp page title not found")

    def retrieve_email(self):
        email_text = self.get_element_text(self.email_text_field)
        # ic(email_text)
        # Using slicing to extract email from the text
        start_index = email_text.find("to ") + 3  # Find where "to " ends
        end_index = len(email_text)  # The email is at the end of the text
        actual_email = email_text[start_index:end_index]
        # ic(actual_email)
        return actual_email

    def enter_otp(self, otp):
        otp_inputs = self.wait_for_all_elements_presence(self.otp_fields)

        # Ensure we have exactly 6 OTP input fields
        if len(otp_inputs) == 6:
            #otp = "345344"
            # Iterate over the OTP characters and input them
            for i, otp_char in enumerate(otp):
                otp_input_element = otp_inputs[i]
                self.wait_for_element_clickable(otp_input_element)  # maybe it will be a comment line
                otp_input_element.send_keys(otp_char)

            # Optionally, submit the OTP if there is a submit button (replace with actual submit logic if required)
            # submit_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.ID, "submit_button_id"))
            # )
            # submit_button.click()

            ic("OTP entered successfully.")
        else:
            ic("Error: Could not find 6 OTP input fields.")
