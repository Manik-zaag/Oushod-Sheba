from behave import *
from icecream import ic

from pages.LogInPage import LogInPage


@given('I am on the login page')
def step_impl(context):
    context.login_page = LogInPage(context.driver)
    context.login_page.navigate_to_base_page(context)
    assert context.login_page.display_status_of_log_in_page()


@when("I select Owner as login type")
def step_select_owner_as_login_type(context):
    context.login_page.click_on_owner_radio_button()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    for data in context.table:
        context.login_page.enter_email_address(data['email'])
        context.login_page.enter_password(data['password'])


@when(u'I click on Log in button')
def step_impl(context):
    context.pharmacy_selection_page = context.login_page.click_on_log_in_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.pharmacy_selection_page.display_status_of_pms_pharmacy(), "Pharmacy Selection Page Not found"


@when(u'I enter invalid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I enter unauthorized email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@then(u'I should get a warning message as "{expected_warning_message}"')
def step_impl(context, expected_warning_message):
    actual_warning_message = context.login_page.retrieve_incorrect_email_or_password_warning_message()
    assert actual_warning_message.__eq__(expected_warning_message), f"Expected: {expected_warning_message}, Actual:{actual_warning_message}"


@then(u'I should get a warning message for invalid email as "{expected_warning_message}"')
def step_impl(context, expected_warning_message):
    actual_warning_message = context.login_page.retrieve_email_warning_message()
    assert actual_warning_message.__eq__(expected_warning_message), f"Expected: {expected_warning_message}, Actual:{actual_warning_message}"


@then(u'Then I should see a password error message indicating the minimum length requirement')
def step_impl(context):
    expected_warning_message_for_password = "Min. 8 characters"

    password_warning_message = context.login_page.retrieve_empty_password_warning_message()
    assert password_warning_message.__eq__(expected_warning_message_for_password)


@when(u'I enter valid email address as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I enter invalid email address as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I do not enter anything into email address and password fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")


@then(u'I should get a proper inline warning message as "{expected_warning_message_for_email}" and "{expected_warning_message_for_password}"')
def step_impl(context, expected_warning_message_for_email, expected_warning_message_for_password):
    actual_warning_message_for_email = context.login_page.retrieve_email_warning_message()
    actual_warning_message_for_password = context.login_page.retrieve_password_warning_message()
    assert actual_warning_message_for_email.__eq__(expected_warning_message_for_email), f"Expected: {expected_warning_message_for_email}, Actual:{actual_warning_message_for_email}"
    assert actual_warning_message_for_password.__eq__(expected_warning_message_for_password), f"Expected: {expected_warning_message_for_password}, Actual:{actual_warning_message_for_password}"
