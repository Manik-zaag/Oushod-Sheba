from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_button = (By.XPATH, "//a[@href='/sign-in']/button[@type='button']")
        self.our_service_section_title = (By.XPATH, "//div[@id='service-card']/div/p[1]")

    def navigate_to_base_page(self, context):
        self.navigate_to_base_url(context.base_url)

    def retrieve_page_title(self):
        return self.get_page_title()

    def display_status_of_home_page(self):
        return self.is_element_displayed(self.our_service_section_title)

    # def enter_product_into_search_box_field(self, product_name):
    #     #  self.send_keys_to_element(self.search_box_field_name, product_name)
    #     pass

    # def click_on_search_button(self):
    #     self.click_on_element(self.search_button_xpath)
    #     return SearchPage(self.driver)

    def click_on_sign_in_button_in_header(self):
        from pages.LogInPage import SignInPage
        self.click_on_element(self.sign_in_button)
        return SignInPage(self.driver)

