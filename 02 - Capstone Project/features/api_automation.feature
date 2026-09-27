Feature: Automation Exercise API Testing

  Scenario: Get all products
    When I request the products list
    Then the products response should be successful

  Scenario: Search for a product
    When I search for "top"
    Then the search response should contain products

  Scenario: Verify valid user login
    When I verify the registered user login
    Then the user should be authenticated successfully

  Scenario: Verify invalid user login
    When I verify an invalid user login
    Then the login should be rejected