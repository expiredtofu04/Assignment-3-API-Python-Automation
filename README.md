# Python API Automation Framework

A Python-based API automation framework developed using **Requests, Behave BDD, and Allure Reporting** for testing user management and product APIs of the Automation Exercise platform.

---

## 1. Project Overview

This project implements a reusable API automation framework for validating REST APIs using Python.

The framework uses:

- **Requests** for sending HTTP API requests
- **Behave** for Behavior-Driven Development (BDD)
- **Allure** for test reporting
- **JSON** files for configuration and test data
- **Python logging** for request and response logging
- **Reusable assertions** for validating API responses

The framework covers both **positive and negative API test scenarios**.

---

## 2. Objectives

The main objectives of this project are:

- Automate REST API testing using Python.
- Implement BDD-based API test scenarios.
- Create a reusable API client.
- Separate configuration and test data from test logic.
- Implement reusable assertions.
- Validate both HTTP status codes and API-level response codes.
- Implement logging and exception handling.
- Generate Allure test reports.
- Create a maintainable and reusable automation framework.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Requests | Sending HTTP API requests |
| Behave | BDD test framework |
| Gherkin | Writing BDD scenarios |
| Allure | Test reporting |
| JSON | Configuration and test data |
| Logging | Request/response logging |
| Git/GitHub | Version control and project submission |

---

## 4. API Platform

The APIs used in this project are provided by:

**Automation Exercise API**

Base URL:

```text
https://automationexercise.com

## 5. Test Data Setup

The project uses `test_data/user_data.json` for user-related API testing.

For security, the actual test data file is excluded from GitHub.

1. Copy `test_data/user_data.example.json`
2. Rename the copy to `user_data.json`
3. Enter valid test-account credentials
4. Run the tests using `behave`

## Project Demonstration

A short demonstration video showing the API automation framework execution,
Behave BDD scenarios, test results, and Allure reporting, along with showing the outputs as well.

[https://drive.google.com/drive/folders/1FlbN6qvMem2UFJIKXtRj9BXk773awlf_?usp=drive_link]
