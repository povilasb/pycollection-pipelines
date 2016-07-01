from collection_pipelines.core import CollectionPipelineProcessor, \
    CollectionPipelineOutput


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


class cat(CollectionPipelineProcessor):
    def __init__(self, fname):
        self.fname = fname
        self.source(self.make_generator)

    def make_generator(self):
        with open(self.fname, 'r') as f:
            for line in f:
                self.receiver.send(line.rstrip('\n'))
            self.receiver.close()


class words(CollectionPipelineProcessor):
    """Splits text into words."""

    def process(self, item):
        for word in item.split():
            self.receiver.send(word.strip(',.;:?!'))


class out(CollectionPipelineOutput):
    def process(self, item):
        print(item)
