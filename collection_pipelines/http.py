import urllib.request

from collection_pipelines.core import CollectionPipelineSource


class http(CollectionPipelineSource):
    def __init__(self, url: str) -> None:
        super().__init__()

        self._set_url(url)

    def on_begin(self):
        self.receiver.send(self._get(self.url))
        self.receiver.close()

    def _set_url(self, url: str):
        if not url.startswith('http://'):
            url = 'http://' + url

        self.url = url

    def _get(self, url: str):
        """
        Returns:
            str: response body.
        """
        return urllib.request.urlopen(url).read().decode('utf-8')
