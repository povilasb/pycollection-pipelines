from hamcrest import assert_that, is_

from collection_pipelines.text import echo, split
from collection_pipelines.std import value


def describe_echo():
    def it_sends_the_specified_argument_to_output():
        text = echo('item') | value()

        assert_that(text, is_('item'))

def describe_split_processor():
    def it_splits_string_by_delimiter_and_outputs_all_the_parts():
        nums = echo('1.2.3.4') | split('.') | value()

        assert_that(nums, is_(['1', '2', '3', '4']))
