@rest
Feature: User posts tweets

  Scenario: user who does not follow anyone does not see tweets
    Given Alice does not follow anyone
    When Alice retrieves the feedback
    Then Alice an empty list of tweets

  Scenario: users see tweets of people they follow
    Given Alice follows Bob
    When Alice retrieves the feed
    Then Alice sees Bob's tweets

    Scenario: users posts a new tweet
      Given Alice follows Bob
      And Bob sends a new tweet
      When Alice retrieves the feed
      Then Alice sees the new tweet