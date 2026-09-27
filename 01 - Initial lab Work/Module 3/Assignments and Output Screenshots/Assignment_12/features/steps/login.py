# Imports
from behave import given, when, then
from selenium import webdriver
from features.pages.login_page import LoginPage


# Open Website
@given("I open the SauceDemo login page")
def open_login_page(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()

    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()


# Login
@when('I enter username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when("I click the login button")
def click_login(context):
    context.login_page.click_login()


# Validation
@then('the login result should be "{expected}"')
def verify_login(context, expected):

    if expected == "success":
        assert context.login_page.is_login_successful()

    else:
        assert context.login_page.is_error_displayed()

    context.driver.quit()