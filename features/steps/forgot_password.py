
from behave import *
from icecream import ic

from utilities.toast_alerts import ToastAlerts


@when(u'I click on the "Forgot Password" link')
def step_impl(context):
    context.forgot_password_page = context.login_page.click_on_forgot_password_button()


@then(u'I should be redirected to the Forgot Password page')
def step_impl(context):
    assert context.forgot_password_page.display_status_of_forgot_password()


@when(u'I enter my email address "{email}" in the email field')
def step_impl(context, email):
    context.written_email_in_forgot_password_page = email
    context.forgot_password_page.enter_email_address_for_otp(email)


@when('I enter invalid address "{email}" in the email field')
def step_impl(context, email):
    context.written_email_in_forgot_password_page = email
    context.forgot_password_page.enter_email_address_for_otp(email)


@when('I enter unknown email address as "{email}" in the email field')
def step_impl(context, email):
    context.written_email_in_forgot_password_page = email
    context.forgot_password_page.enter_email_address_for_otp(email)


@when('I do not enter anything into email address')
def step_impl(context):
    context.forgot_password_page.enter_email_address_for_otp("")


@when(u'I click the "Get Code" button')
def step_impl(context):
    context.otp_page = context.forgot_password_page.click_on_get_code_button()


@then(u'I should be redirected to the OTP page')
def step_impl(context):
    assert context.otp_page.display_status_of_forgot_otp()
    actual_email = context.otp_page.retrieve_email()
    ic(context.written_email_in_forgot_password_page)
    assert actual_email.__eq__(context.written_email_in_forgot_password_page)


@then(u'I should see a successful toast message "{expected_toast_title}" & "{expected_toast_description}"')
def step_impl(context, expected_toast_title, expected_toast_description):
    try:
        toast_alerts = ToastAlerts(context.driver)
        success_toast = toast_alerts.handle_toast_success()
    except Exception as e:
        ic(f"Error handling error toast: {str(e)}")

    assert success_toast['title'].__eq__(expected_toast_title), f"Expected message: '{expected_toast_title}', but got: '{success_toast['title']}'"
    assert success_toast['description'].__eq__(expected_toast_description), f"Expected message: '{expected_toast_description}', but got: '{success_toast['description']}'"
    assert (context.otp_page.display_status_of_forgot_otp())


@then(u'I should see a error toast message "{expected_toast_title}" & "{expected_toast_description}"')
def step_impl(context, expected_toast_title, expected_toast_description):
    try:
        toast_alerts = ToastAlerts(context.driver)
        error_toast = toast_alerts.handle_toast_error()
    except Exception as e:
        ic(f"Error handling error toast: {str(e)}")

    assert error_toast['title'].__eq__(expected_toast_title), f"Expected message: '{expected_toast_title}', but got: '{error_toast['title']}'"
    assert error_toast['description'].__eq__(expected_toast_description + context.written_email_in_forgot_password_page), f"Expected message: '{expected_toast_description + context.written_email_in_forgot_password_page}', but got: '{error_toast['description']}'"


@then('I should get a proper inline warning message as "{expected_message}" in forgot password email field')
def step_impl(context, expected_message):
    actual_message = context.forgot_password_page.retrieve_empty_email_warning_message_in_forgot_password()

    actual_message = actual_message
    assert actual_message.__eq__(expected_message), f"Expected message: '{expected_message}', but got: '{actual_message}'"
