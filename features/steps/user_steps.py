from behave import given, when, then

from framework.api_client import APIClient
from framework.config_reader import get_config
from framework.assertions import (
    assert_status_code,
    assert_response_code,
    assert_response_message
)


@given("the User Management API is available")
def step_api_available(context):
    config = get_config()

    context.client = APIClient(
        config["base_url"]
    )


@when("I request user details using an email")
def step_get_user(context):

    params = {
        "email": context.user_data["email"]
    }

    context.response = context.client.get(
        "/api/getUserDetailByEmail",
        params=params
    )


@then("the response status code should be 200")
def step_status_200(context):
    assert_status_code(
        context.response,
        200
    )


@when("I verify login using invalid credentials")
def step_invalid_login(context):

    data = {
        "email": "definitely_invalid_user_987654@example.com",
        "password": "DefinitelyWrongPassword123!"
    }

    context.response = context.client.post(
        "/api/verifyLogin",
        data=data
    )


@then("the response status code should be 404")
def step_status_404(context):
    assert_response_code(
        context.response,
        404
    )


@when("I verify login without providing email")
def step_login_without_email(context):

    data = {
        "password": "SomePassword123"
    }

    context.response = context.client.post(
        "/api/verifyLogin",
        data=data
    )


@then("the response status code should be 400")
def step_status_400(context):
    assert_response_code(
        context.response,
        400
    )


@when("I create a new user account")
def step_create_user(context):

    context.response = context.client.post(
        "/api/createAccount",
        data=context.user_data
    )


@when("I verify login using valid credentials")
def step_valid_login(context):

    data = {
        "email": context.user_data["email"],
        "password": context.user_data["password"]
    }

    context.response = context.client.post(
        "/api/verifyLogin",
        data=data
    )


@when("I request the created user's details")
def step_get_created_user(context):

    params = {
        "email": context.user_data["email"]
    }

    context.response = context.client.get(
        "/api/getUserDetailByEmail",
        params=params
    )


@when("I update the user account")
def step_update_user(context):

    updated_data = context.user_data.copy()

    updated_data["name"] = "Updated API User"

    context.response = context.client.put(
        "/api/updateAccount",
        data=updated_data
    )


@when("I delete the user account")
def step_delete_user(context):

    data = {
        "email": context.user_data["email"],
        "password": context.user_data["password"]
    }

    context.response = context.client.delete(
        "/api/deleteAccount",
        data=data
    )


@then("the response status code should be 201")
def step_status_201(context):

    assert_response_code(
        context.response,
        201
    )


@then('the response message should be "User created!"')
def step_user_created_message(context):

    assert_response_message(
        context.response,
        "User created!"
    )


@then('the response message should be "User not found!"')
def step_user_not_found_message(context):

    assert_response_message(
        context.response,
        "User not found!"
    )


@then('the response message should be "Bad request, email or password parameter is missing in POST request."')
def step_missing_email_message(context):

    assert_response_message(
        context.response,
        "Bad request, email or password parameter is missing in POST request."
    )