Feature: Pharmacy selection on the Pharmacy Management System (PMS) page
  As a user
  I want to select a pharmacy
  So that I can view its details and perform actions

  Background:
    Given I am on the login page
    When I select Owner as login type
    When I enter valid email address and valid password into the fields
      | email              | password |
      | pms_tc11@gmail.com | aA123456 |
    And I click on Log in button
    Then I should get logged in


  @smoke
  Scenario Outline: Select each pharmacy by name
    When I select the pharmacy with name "<pharmacy_name>"
    Then I should see the "<pharmacy_name>" in Dashboard

    Examples:
      | pharmacy_name   |
      | Tiger Jordan    |
      | Kiayada Schmidt |
      | Zaag            |

  @smoke
  Scenario Outline: Retrieve pharmacy address by name
    When I search for the pharmacy with name "<pharmacy_name>"
    Then I should get the address of "<pharmacy_name>" as "<pharmacy_address>"

    Examples:
      | pharmacy_name   | pharmacy_address                                                     |
      | Tiger Jordan    | street, state, City-25556                                            |
      | Kiayada Schmidt | Perferendis est inci, Explicabo Veniam o, Quia modi eligendi i-59404 |
      | Zaag            | Bangladesh, Mirpur12, Dhaka-Dhaka1212              |

  @smoke
  Scenario Outline: Select a pharmacy by name
    When I select a pharmacy with name "<pharmacy_name>"
    Then I should see the "<pharmacy_name>" in Dashboard

    Examples:
      | pharmacy_name   |
      | Kiayada Schmidt |