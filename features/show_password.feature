Feature: Show Password functionality for password field
  As a user
  I want to be able to click on the eye icon to reveal the password in the password field
  So that I can view the password when needed

  @login
  Scenario: User clicks the eye icon to show the password
    Given I am on the login page
    When I have entered a password as "pass54321" in the password field
    And I click the eye icon next to the password field
    Then the password should be visible in the password field
    And the eye icon should change to indicate the password is visible
