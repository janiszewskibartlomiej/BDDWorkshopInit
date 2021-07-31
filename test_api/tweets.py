import json

import connexion as connexion

from followed import does_alice_follow_bob, FILE_NAME


def get():
    if does_alice_follow_bob():
        with open(FILE_NAME) as output_file:
            tweets = [{"username": "Bob", "tweet": "something"}]
            tweets_in_file = json.load(output_file)
            return tweets + tweets_in_file
    else:
        return []


def add():
    tweet = connexion.request.json["tweet"]
    with open(FILE_NAME, "w") as output_file:
        json.dump([{"username": "Bob", "twee"
                                       "t": "tweet"}], output_file)