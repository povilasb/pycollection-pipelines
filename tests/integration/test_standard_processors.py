from hamcrest import assert_that, is_

from collection_pipelines.std import value, head, tail, freq
from collection_pipelines.text import echo, split


def describe_head():
    def it_sends_the_specified_count_of_arguments():
        items = echo('1.2.3.4') | split('.') | head(2) | value()

        assert_that(items, is_(['1', '2']))

def describe_tail():
    def it_sends_N_last_items():
        items = echo('1.2.3.4') | split('.') | tail(2) | value()

        assert_that(items, is_(['3', '4']))

def describe_freq():
    def it_sends_unique_items_with_their_frequency():
        items = echo('1.2.3.1.3') | split('.') | freq() | value()

        assert_that(items, is_([('1',  2), ('2', 1), ('3', 2)]))
