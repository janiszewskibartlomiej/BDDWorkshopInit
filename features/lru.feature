Feature: LRU

#  Scenario: Add new file to LRU
#    Given a new empty list is created
#    When add file to list
#    Then file is visible in list


  Scenario: we add a file to an empty list
    Given the list is empty
    When we add a file to the list
    Then the list contains only the added file
    And the list contains old elements and new one

  Scenario: we add a file to not empty list
    Given the list is not empty
    When we add a file to the list
    Then the list contains old elements and new one

  Scenario: a newly added element is first added to the list
    Given the list is not empty
    When we add a file to the list
    Then the list contains added file at first position

#  Scenario: a duplicate is added to the list
#    Given the list of files with the duplicable element at the last position
#    When we add a duplicate to the list
#    Then the file is visible only once one the list
#
#    Scenario: the list has a max size 5
#      Given the list has 5 element
#      When add new file
#      Then list has 5 elements
#      And a new file in on list
