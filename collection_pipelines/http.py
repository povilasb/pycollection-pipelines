import urllib.request

from collection_pipelines.core import CollectionPipelineProcessor


class http(CollectionPipelineProcessor):
    def __init__(self, url):
        self._set_url(url)
        self.source(self.make_generator)

    def make_generator(self):
        self.receiver.send(self._get(self.url))
        self.receiver.close()

    def _set_url(self, url):
        if not url.startswith('http://'):
            url = 'http://' + url

        self.url = url

    def _get(self, url):
        """
        Returns:
            str: response body.
        """
        return urllib.request.urlopen(url).read().decode('utf-8')
