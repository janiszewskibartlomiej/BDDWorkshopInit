import random
import string

from behave import *


class LRU:
    def __init__(self):
        self.list = []

    def add_element(self, other):
        self.list.insert(0, other)

    def __iter__(self):
        yield from self.list

def _random_string():
    return ''.join(random.choice(string.ascii_letters) for _ in range(8))

@given(u'the list is empty')
def step_impl(context):
    context.object_under_test = LRU()


@when(u'we add a file to the list')
def step_impl(context):
    context.new_element = _random_string()
    if 'added_elements' in context:
        context.added_elements.append(context.new_element)
    else:
        context.added_elements = [context.new_element]
    context.object_under_test.add_element(context.new_element)


@then(u'the list contains only the added file')
def step_impl(context):
    actual = [x for x in context.object_under_test]
    assert actual == context.added_elements


@given(u'the list is not empty')
def step_impl(context):
    context.execute_steps(u"""
    Given the list is empty 
    When we add a file to the list
    """)

@then(u'the list contains old elements and new one')
def step_impl(context):
    print(list(context.object_under_test))
    print(context.added_elements)
    assert set(list(context.object_under_test)) == set(context.added_elements)


@then("the list contains added file at first position")
def step_impl(context):
    context.object_under_test.add_element(context.new_element)
    assert context.new_element == list(context.object_under_test)[0]


@given(u'a new empty list is created')
def step_impl(context):
    pass


@when(u'add file to list')
def step_impl(context):
    pass


@then(u'file is visible in list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then file is visible in list')


@given(u'the list of files with the duplicable element at the last position')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the list of files with the duplicable element at the last position')


@when(u'we add a duplicate to the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we add a duplicate to the list')


@then(u'the file is visible only once one the list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the file is visible only once one the list')


@given(u'the list has 5 element')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the list has 5 element')


@when(u'add new file')
def step_impl(context):
    raise NotImplementedError(u'STEP: When add new file')


@then(u'list has 5 elements')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then list has 5 elements')


@then(u'a new file in on list')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a new file in on list')