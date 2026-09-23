from behave import given, when, then

from framework.api_client import APIClient
from framework.config_reader import get_config
from framework.assertions import assert_status_code
from framework.assertions import assert_response_code


@given("the Product API is available")
def step_product_api(context):

    config = get_config()

    context.client = APIClient(
        config["base_url"]
    )


@when("I request all products")
def step_all_products(context):

    context.response = context.client.get(
        "/api/productsList"
    )


@then("the product response status code should be 200")
def step_product_status_200(context):

    assert_status_code(
        context.response,
        200
    )


@when('I search for a product named "top"')
def step_search_product(context):

    data = {
        "search_product": "top"
    }

    context.response = context.client.post(
        "/api/searchProduct",
        data=data
    )


@then("the product search response status code should be 200")
def step_search_status_200(context):

    assert_status_code(
        context.response,
        200
    )


@when("I search without providing a product name")
def step_search_without_parameter(context):

    context.response = context.client.post("/api/searchProduct")


@then("the product response status code should be 400")
def step_product_status_400(context):

    assert_response_code(context.response, 400)

@then("the product API response code should be 400")
def step_product_response_code_400(context):
    assert_response_code(context.response, 400)