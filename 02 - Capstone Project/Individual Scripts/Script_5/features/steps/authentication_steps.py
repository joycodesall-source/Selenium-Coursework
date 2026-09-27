import requests
import allure
from behave import given, when, then


@given("I have valid user credentials")
def step_valid_credentials(context):
    context.email = "joycodesall@gmail.com"
    context.password = "Excellent@233"


@when("I send a login request")
def step_login_request(context):
    url = "https://automationexercise.com/api/verifyLogin"

    data = {
        "email": context.email,
        "password": context.password
    }

    with allure.step("Send login request"):
        context.response = requests.post(url, data=data)


@then("the user should be authenticated")
def step_verify_login(context):
    with allure.step("Verify authentication response"):
        print("Status Code:", context.response.status_code)
        print("Response:", context.response.json())

        allure.attach(
            context.response.text,
            name="API Response",
            attachment_type=allure.attachment_type.JSON
        )

        assert context.response.status_code == 200
        assert context.response.json()["message"] == "User exists!"