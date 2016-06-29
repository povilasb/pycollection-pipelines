from collection_pipelines.core import CollectionPipelineProcessor


class echo(CollectionPipelineProcessor):
    def __init__(self, text):
        self.text = text
        self.source(self.make_generator)

    def make_generator(self):
        self.receiver.send(self.text)
        self.receiver.close()
