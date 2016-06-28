from hamcrest import assert_that, is_
from mock import MagicMock

from collection_pipelines.json import json, dict_item


def describe_json():
    def describe_process():
        def describe_when_specified_json_path_exists():
            def it_sends_value_for_that_path_to_output():
                proc = json('name')
                proc.receiver = MagicMock()

                proc.process('{"name": "Bob"}')

                proc.receiver.send.assert_called_with('Bob')

        def describe_when_subpath_is_given():
            def it_sends_value_for_that_path_to_output():
                proc = json('name.first')
                proc.receiver = MagicMock()

                proc.process('{"name": {"first": "Bob"}}')

                proc.receiver.send.assert_called_with('Bob')

def describe_dict_item():
    def describe_when_path_points_to_nested_element():
        def it_returns_nested_elements_value():
            data = {'name': {'first': 'Bob'}}

            first_name = dict_item(data, 'name.first')

            assert_that(first_name, is_('Bob'))
