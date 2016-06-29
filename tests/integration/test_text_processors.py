from hamcrest import assert_that, is_

from collection_pipelines.text import echo
from collection_pipelines.std import value


def describe_echo():
    def it_sends_the_specified_argument_to_output():
        text = echo('item') | value()

        assert_that(text, is_('item'))
