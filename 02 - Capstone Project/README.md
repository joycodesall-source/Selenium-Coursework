**Selenium Capstone Project**
By Joyashis Mallick|Enrollment No: 12023002023022

# Python API Automation Framework

# Python API Automation Framework

A Python API automation framework built with **Requests**, **Behave BDD**, **Allure Reporting**, and a reusable API client design.

## Objective

Automate REST API scenarios covering:

- REST API testing
- Product retrieval and search
- User authentication
- Valid and invalid login handling
- BDD test execution
- Allure reporting
- Reusable framework design

## Technology Stack

- Python 3.14
- Requests 2.32.5
- Behave 1.3.3
- Allure Behave 2.16.1
- Allure Report CLI 3.18.0

## API

[Automation Exercise API](https://automationexercise.com/api_list)

The framework uses the following API operations:

- `GET /api/productsList`
- `POST /api/searchProduct`
- `POST /api/verifyLogin`

## Project Structure

```text
Capstone Project/
├── project.py
├── behave.ini
├── requirements.txt
├── features/
│   ├── api_automation.feature
│   └── steps/
│       └── api_steps.py
├── Individual Scripts/
├── Output Screenshots/
└── allure-results/
```

## BDD Scenarios

1. Get all products
2. Search for a product
3. Verify valid user login
4. Verify invalid user login

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Set valid test credentials in `project.py` before running the authentication scenarios.

## Execution

Run the complete BDD suite from the project root:

```bash
behave --no-capture
```

The final execution validates all four scenarios and their expected API responses.

## Allure Report

After execution, generate and open the Allure report with:

```bash
allure serve allure-results
```

## Outputs

The `Output Screenshots` folder contains the execution evidence, including the final Capstone execution and Allure report.

## Demonstration Video

[Project Demonstration Video Link](https://drive.google.com/file/d/1OqqcmWsQkeE4NStbv57g-imoXCvtdkq8/view?usp=sharing)
