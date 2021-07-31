from behave import *
import requests


def retrieve_feed():
    response = requests.get("http://127.0.0.1:5000/api/feed")
    return response.json()

def alice_follows_bob():
    requests.put("http://127.0.0.1:5000/api/followed/Alice/Bob")


@given(u'Alice does not follow anyone')
def step_impl(context):
    requests.delete("http://127.0.0.1:5000/api/followed")


@when(u'Alice retrieves the feedback')
def step_impl(context):
    context.feed = retrieve_feed()

@then(u'Alice an empty list of tweets')
def step_impl(context):
    assert len(context.feed) == 0


@given(u'Alice follows Bob')
def step_impl(context):
    alice_follows_bob()

@when(u'Alice retrieves the feed')
def step_impl(context):
    context.feed = retrieve_feed()

@then(u'Alice sees Bob\'s tweets')
def step_impl(context):
    print(context.feed)
    assert len(context.feed) == 1


@given(u'Bob sends a new tweet')
def step_impl(context):
    context.new_tweet = "some new tweet"
    requests.post("http://127.0.0.1:5000/api/feed", json={"tweet": "some wen tweet"})


@then(u'Alice sees the new tweet')
def step_impl(context):
    print(context.feed)
    filtered_feed = [x for x in context.feed if x["tweet"] == context.new_tweet]