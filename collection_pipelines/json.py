from json import loads as json_loads
from functools import reduce

from collection_pipelines.core import CollectionPipelineProcessor


class json(CollectionPipelineProcessor):
    def __init__(self, path: str) -> None:
        self.path = path

    def process(self, item: str):
        data = json_loads(item)
        self.receiver.send(dict_item(data, self.path))


def dict_item(dictionary: dict, path: str):
    """Extracts dictionary item by the given path.

    Args:
        path: path to dictionary item. May point to nested elements.
            In such case dot is used to notate children nodes.
            E.g. "name.first".

    Returns:
        Dictionary element value.
    """
    return reduce(lambda d, key: d[key], path.split('.'), dictionary)
