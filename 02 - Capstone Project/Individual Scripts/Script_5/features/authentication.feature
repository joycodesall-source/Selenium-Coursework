Feature: User Authentication

  Scenario: Verify a registered user
    Given I have valid user credentials
    When I send a login request
    Then the user should be authenticated