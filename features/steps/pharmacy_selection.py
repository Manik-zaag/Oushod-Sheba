from behave import *
from icecream import ic


@when('I select the pharmacy with name "{pharmacy_name}"')
def step_impl(context, pharmacy_name):
    context.dashboard_page = context.pharmacy_selection_page.select_pharmacy_button(pharmacy_name)


@when('I select a pharmacy with name "{pharmacy_name}"')
def step_impl(context, pharmacy_name):
    context.dashboard_page = context.pharmacy_selection_page.select_pharmacy_button(pharmacy_name)


@when('I search for the pharmacy with name "{pharmacy_name}"')
def step_impl(context, pharmacy_name):
    actual_pharmacy_name = context.pharmacy_selection_page.get_pharmacy_name(pharmacy_name).text.strip()
    assert actual_pharmacy_name == pharmacy_name, f"Expected pharmacy '{pharmacy_name}' in pms-pharmacy, but found '{actual_pharmacy_name}'"


@then('I should see the "{expected_pharmacy_name}" in Dashboard')
def step_impl(context, expected_pharmacy_name):
    actual_pharmacy_name = context.dashboard_page.retrieve_pharmacy_name()
    assert expected_pharmacy_name.__eq__(actual_pharmacy_name), f"Expected pharmacy '{expected_pharmacy_name}' in Dashboard, but found '{actual_pharmacy_name}'"


@then('I should get the address of "{pharmacy_name}" as "{expected_pharmacy_address}"')
def step_impl(context, pharmacy_name, expected_pharmacy_address):
    actual_pharmacy_address = context.pharmacy_selection_page.retrieve_pharmacy_address(pharmacy_name)

    assert actual_pharmacy_address == expected_pharmacy_address, f"Expected address for '{pharmacy_name}' is '{expected_pharmacy_address}' but found '{actual_pharmacy_address}'"
