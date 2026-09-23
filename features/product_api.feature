Feature: Product Management API

  As an API automation tester
  I want to validate product-related APIs
  So that I can verify successful and unsuccessful product operations

  Scenario: Get all products successfully
    Given the Product API is available
    When I request all products
    Then the product response status code should be 200

  Scenario: Search for a product successfully
    Given the Product API is available
    When I search for a product named "top"
    Then the product search response status code should be 200

  Scenario: Search for a product without providing a product name
    Given the Product API is available
    When I search without providing a product name
    Then the product API response code should be 400