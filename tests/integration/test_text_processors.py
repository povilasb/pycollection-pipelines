from hamcrest import assert_that, is_

from collection_pipelines.text import echo, split, words
from collection_pipelines.std import value, filter


def describe_echo():
    def describe_when_single_item_is_provided():
        def it_sends_it_to_output():
            text = echo('item') | value()

            assert_that(text, is_('item'))

    def describe_when_array_of_items_is_given():
        def it_sends_item_by_item_to_output():
            items = echo([1, 2, 3]) | filter(2) | value()

            assert_that(items, is_([1, 3]))

def describe_split_processor():
    def it_splits_string_by_delimiter_and_outputs_all_the_parts():
        nums = echo('1.2.3.4') | split('.') | value()

        assert_that(nums, is_(['1', '2', '3', '4']))

def describe_words_processor():
    def if_splits_text_into_words():
        word_list = echo('word1 word2 word3') | words() | value()

        assert_that(word_list, is_(['word1', 'word2', 'word3']))

    def it_ommits_punctuation_symbols():
        word_list = echo('word1, word2, word3.') | words() | value()

        assert_that(word_list, is_(['word1', 'word2', 'word3']))
