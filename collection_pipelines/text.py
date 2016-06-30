from collection_pipelines.core import CollectionPipelineProcessor


class split(CollectionPipelineProcessor):
    def __init__(self, delimiter):
        self.delimiter = delimiter

    def process(self, item):
        for part in item.split(self.delimiter):
            self.receiver.send(part)


class echo(CollectionPipelineProcessor):
    def __init__(self, text):
        self.text = text
        self.source(self.make_generator)

    def make_generator(self):
        self.receiver.send(self.text)
        self.receiver.close()
