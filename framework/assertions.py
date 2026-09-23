def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, (
        f"Expected HTTP status code {expected_status_code}, "
        f"but got {response.status_code}"
    )


def assert_response_code(response, expected_response_code):
    response_data = response.json()
    actual_response_code = response_data.get("responseCode")

    assert actual_response_code == expected_response_code, (
        f"Expected API responseCode {expected_response_code}, "
        f"but got {actual_response_code}"
    )


def assert_response_contains(response, key):
    response_data = response.json()

    assert key in response_data, (
        f"Expected '{key}' in response"
    )


def assert_response_message(response, expected_message):
    response_data = response.json()
    actual_message = response_data.get("message")

    assert actual_message == expected_message, (
        f"Expected message '{expected_message}', "
        f"but got '{actual_message}'"
    )