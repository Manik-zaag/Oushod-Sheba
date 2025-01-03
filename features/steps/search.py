import time

from behave import *

from pages.HomePage import HomePage

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@when(u'I enter valid product as "{product}" into the Search box field')
def step_impl(context, product):
    context.login_page.enter_product_into_search_box_field(product)


@when('I enter invalid product as "{product}" into the Search box field')
def step_impl(context, product):
    context.login_page.enter_product_into_search_box_field(product)


@when('I click on Search button')
def step_impl(context):
    context.search_page = context.login_page.click_on_search_button()


@then('Proper message should be displayed in Search results')
def step_impl(context):
    assert context.search_page.retrieve_no_product_message()


@when('I don\'t enter anything into Search box field')
def step_impl(context):
    context.login_page.enter_product_into_search_box_field("")
    logger.info("Hello Manik")
    print("Hello Kinam")


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    assert context.search_page.display_status_of_valid_product()
