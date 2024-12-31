Feature: Forgot Password functionality
  As a user
  I want to be able to reset my password
  So that I can recover my account if I forget my password

  @forgot_password
  Scenario: User clicks on Forgot Password, enters valid email, and clicks Get Code
    Given I am on the Home page
    And I click the "Sign In" button in header
    When I click on the "Forgot Password" link
    Then I should be redirected to the Forgot Password page
    When I enter my email address "sqa+1@zaagsys.com" in the email field
    And I click the "Get Code" button
    Then I should be redirected to the OTP page
    And I should see a successful toast message "Success" & "Otp Send"

  @forgot_password
  Scenario: User clicks on Forgot Password, without entering email, clicks Get Code
    Given I am on the Home page
    And I click the "Sign In" button in header
    When I click on the "Forgot Password" link
    Then I should be redirected to the Forgot Password page
    When I do not enter anything into email address
    And I click the "Get Code" button
    Then I should get a proper inline warning message as "Please enter email id" in forgot password email field

  @forgot_password
  Scenario: User clicks on Forgot Password, with unknown email, clicks Get Code
    Given I am on the Home page
    And I click the "Sign In" button in header
    When I click on the "Forgot Password" link
    Then I should be redirected to the Forgot Password page
    When I enter unknown email address as "sqa+111231@zaagsys.com" in the email field
    And I click the "Get Code" button
    Then I should see a error toast message "Error" & "Customer not found by email: "

  @forgot_password
  Scenario Outline: User clicks on Forgot Password, enters invalid email, and clicks Get Code
    Given I am on the Home page
    And I click the "Sign In" button in header
    When I click on the "Forgot Password" link
    Then I should be redirected to the Forgot Password page
    When I enter invalid address "<email>" in the email field
    And I click the "Get Code" button
    Then I should get a proper inline warning message as "Invalid email" in forgot password email field
    Examples:
      | email                                                   |
      | invalid@.com                                            |
      | invalidemail.com                                        |
      | invalid@domain                                          |
      | invalid@@domain.com                                     |
      | inv@lid@domain.com                                      |
      | inv@lid!domain.com                                      |
      | invalid email@domain.com                                |
      | .invalid@domain.com                                     |
      | invalid@domain.c0m                                      |
      | invalid@domain..com                                     |
