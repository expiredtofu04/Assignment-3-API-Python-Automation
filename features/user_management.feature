Feature: User Management API

  As an API automation tester
  I want to validate user management APIs
  So that I can verify successful and unsuccessful user operations

  Scenario: Get user details by email
    Given the User Management API is available
    When I request user details using an email
    Then the response status code should be 200

  Scenario: Verify login with invalid credentials
    Given the User Management API is available
    When I verify login using invalid credentials
    Then the response status code should be 404
    And the response message should be "User not found!"

  Scenario: Verify login without providing email
    Given the User Management API is available
    When I verify login without providing email
    Then the response status code should be 400
    And the response message should be "Bad request, email or password parameter is missing in POST request."

  Scenario: Create a new user account
    Given the User Management API is available
    When I create a new user account
    Then the response status code should be 201
    And the response message should be "User created!"

  Scenario: Verify login with valid credentials
    Given the User Management API is available
    When I verify login using valid credentials
    Then the response status code should be 200

  Scenario: Get the created user's details
    Given the User Management API is available
    When I request the created user's details
    Then the response status code should be 200

  Scenario: Update the user account
    Given the User Management API is available
    When I update the user account
    Then the response status code should be 200

  Scenario: Delete the user account
    Given the User Management API is available
    When I delete the user account
    Then the response status code should be 200