"""Standard pipeline processors."""

from collection_pipelines.core import CollectionPipelineOutput


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
