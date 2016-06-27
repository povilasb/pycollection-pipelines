from hamcrest import assert_that, is_
from mock import MagicMock, patch

from collection_pipelines import http
import collection_pipelines


def describe_http():
    def describe_contructor():
        def it_sets_url_to_get():
            proc = http('http://example.com')

            assert_that(proc.url, is_('http://example.com'))

        def it_appends_http_prefix_if_one_is_not_specified():
            proc = http('example.com')

            assert_that(proc.url, is_('http://example.com'))

        def it_sets_data_source_callback():
            proc = http('dummy.url')

            assert_that(proc.start_source, is_(proc.make_generator))

    def describe_make_generator():
        @patch('collection_pipelines.http_get')
        def it_sends_http_response_to_pipe_output(http_get):
            http_get.return_value = 'response'

            proc = http('example.com')
            proc.receiver = MagicMock()

            proc.make_generator()

            proc.receiver.send.assert_called_with('response')
