from behave import *
from icecream import ic


@when(u'I have entered a password as "{password}" in the password field')
def step_impl(context, password):
    context.password_in_sign_in = password  # entered password
    context.login_page.enter_password(password)
    assert context.login_page.display_status_of_eye_invisible()


@when(u'I click the eye icon next to the password field')
def step_impl(context):
    context.login_page.click_on_eye_button()


@then(u'the password should be visible in the password field')
def step_impl(context):
    expected_password = context.password_in_sign_in
    actual_password = context.login_page.retrieve_password_visibility()
    ic(expected_password, actual_password)
    assert expected_password.__eq__(actual_password)


@then(u'the eye icon should change to indicate the password is visible')
def step_impl(context):
    assert context.login_page.display_status_of_eye_visible()
