"""Standard pipeline processors."""

import collections

from collection_pipelines.core import CollectionPipelineOutput, \
    CollectionPipelineProcessor


class value(CollectionPipelineOutput):
    """Output processor that returns pipeline items."""

    def __init__(self):
        self.retval = []

    def process(self, item):
        """Appends the item to results list."""
        self.retval.append(item)

    def return_value(self):
        """
        Returns:
            [any]: pipeline items.
            any: if only one item went through the pipeline.
        """
        if len(self.retval) == 1:
            return self.retval[0]

        return self.retval


class head(CollectionPipelineProcessor):
    """Processor that passes only the first N items through the pipeline."""

    def __init__(self, count):
        self.count = count
        self.processed = 0

    def process(self, item):
        if self.processed < self.count:
            self.receiver.send(item)
            self.processed += 1


class tail(CollectionPipelineProcessor):
    """Sends only N last items to output.

    It holds only a fixed number of items and when source processor
    sends a done signal, it sends those last N items to output.
    """

    def __init__(self, count):
        self.count = count
        self.processed = collections.deque(maxlen=count)

    def process(self, item):
        self.processed.append(item)

    def on_done(self):
        for item in self.processed:
            self.receiver.send(item)


class freq(CollectionPipelineProcessor):
    """Calculates how much each item appears on the pipeline."""

    def __init__(self):
        self.processed = {}
        self.order = []

    def process(self, item):
        if item in self.processed:
            self.processed[item] += 1
        else:
            self.order.append(item)
            self.processed[item] = 1

    def on_done(self):
        for item in self.order:
            self.receiver.send((item, self.processed[item]))
