from hamcrest import assert_that, is_

from collection_pipelines.std import value, head
from collection_pipelines.text import echo, split


def describe_head():
    def it_sends_the_specified_count_of_arguments():
        items = echo('1.2.3.4') | split('.') | head(2) | value()

        assert_that(items, is_(['1', '2']))
