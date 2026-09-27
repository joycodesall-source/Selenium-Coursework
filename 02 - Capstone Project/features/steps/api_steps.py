import time
import allure
from behave import when, then

from project import client, EMAIL, PASSWORD


@when("I request the products list")
def step_products(context):
    with allure.step("GET products list"):
        context.response = client.get("/api/productsList")

@then("the products response should be successful")
def step_products_success(context):
    response = context.response.json()
    print("API: GET /api/productsList")
    print("Status Code:", context.response.status_code)
    print("Response Code:", response["responseCode"])
    print("Products Retrieved:", len(response["products"]))

    assert context.response.status_code == 200
    assert response["responseCode"] == 200

    allure.attach(
        context.response.text,
        name="Products API Response",
        attachment_type=allure.attachment_type.JSON
    )

@when('I search for "top"')
def step_search_product(context):
    data = {
        "search_product": "top"
    }

    with allure.step("POST product search"):
        context.response = client.post(
            "/api/searchProduct",
            data
        )

@then("the search response should contain products")
def step_search_success(context):
    response = context.response.json()
    print("API: POST /api/searchProduct")
    print("Search Term: top")
    print("Status Code:", context.response.status_code)
    print("Response Code:", response["responseCode"])
    print("Products Found:", len(response["products"]))

    assert context.response.status_code == 200
    assert response["responseCode"] == 200
    assert len(response["products"]) > 0

    allure.attach(
        context.response.text,
        name="Search API Response",
        attachment_type=allure.attachment_type.JSON
    )

@when("I verify the registered user login")
def step_valid_login(context):
    data = {
        "email": EMAIL,
        "password": PASSWORD
    }

    with allure.step("POST valid login"):
        context.response = client.post(
            "/api/verifyLogin",
            data
        )

@then("the user should be authenticated successfully")
def step_valid_login_success(context):
    response = context.response.json()
    print("API: POST /api/verifyLogin")
    print("Status Code:", context.response.status_code)
    print("Response Code:", response["responseCode"])
    print("Message:", response["message"])

    assert context.response.status_code == 200
    assert response["responseCode"] == 200
    assert response["message"] == "User exists!"

    allure.attach(
        context.response.text,
        name="Valid Login Response",
        attachment_type=allure.attachment_type.JSON
    )

@when("I verify an invalid user login")
def step_invalid_login(context):
    data = {
        "email": "invalid_user@example.com",
        "password": "invalid_password"
    }

    with allure.step("POST invalid login"):
        context.response = client.post(
            "/api/verifyLogin",
            data
        )

@then("the login should be rejected")
def step_invalid_login_rejected(context):
    response = context.response.json()
    print("API: POST /api/verifyLogin")
    print("Test Type: Invalid Login")
    print("Status Code:", context.response.status_code)
    print("Response Code:", response["responseCode"])
    print("Message:", response["message"])

    assert context.response.status_code == 200
    assert response["responseCode"] == 404
    assert response["message"] == "User not found!"

    allure.attach(
        context.response.text,
        name="Invalid Login Response",
        attachment_type=allure.attachment_type.JSON
    )
    time.sleep(5)