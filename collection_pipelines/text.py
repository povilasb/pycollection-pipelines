import re

from collection_pipelines.core import CollectionPipelineProcessor, \
    CollectionPipelineOutput, CollectionPipelineSource


class split(CollectionPipelineProcessor):
    def __init__(self, delimiter: str) -> None:
        self.delimiter = delimiter

    def process(self, item: str):
        for part in item.split(self.delimiter):
            self.receiver.send(part)


class echo(CollectionPipelineSource):
    def __init__(self, items) -> None:
        super().__init__()

        self.items = items

    def on_begin(self):
        self._send_items()
        self.receiver.close()

    def _send_items(self):
        """Sends items to pipeline.

        If items is an array, sends them one by one.
        Otherwise simply sends one item.
        """
        if isinstance(self.items, list):
            for item in self.items:
                self.receiver.send(item)
        else:
            self.receiver.send(self.items)


class cat(CollectionPipelineSource):
    def __init__(self, fname: str) -> None:
        super().__init__()

        self.fname = fname

    def on_begin(self):
        with open(self.fname, 'r') as f:
            for line in f:
                self.receiver.send(line.rstrip('\n'))
            self.receiver.close()


class words(CollectionPipelineProcessor):
    """Splits text into words."""

    def process(self, item: str):
        for word in re.split('[ \t,.;:?!]', item):
            if word:
                self.receiver.send(word)


class out(CollectionPipelineOutput):
    def process(self, item):
        print(item)
