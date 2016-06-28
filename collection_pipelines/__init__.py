from collection_pipelines.http import *
from collection_pipelines.json import *


class cat(CollectionPipelineProcessor):
    def __init__(self, fname):
        self.fname = fname
        self.source(self.make_generator)

    def make_generator(self):
        with open(self.fname, 'r') as f:
            for line in f:
                self.receiver.send(line.rstrip('\n'))
            self.receiver.close()


class filter(CollectionPipelineProcessor):
    def __init__(self, text):
        self.text = text

    def process(self, item):
        if item != self.text:
            self.receiver.send(item)


class out(CollectionPipelineProcessor):
    def process(self, item):
        print(item)

    def source(self, start_source):
        start_source()


class count(CollectionPipelineProcessor):
    def __init__(self):
        self.val = 0

    def process(self, item):
        self.val += 1

    def on_done(self):
        self.receiver.send(self.val)


class unique(CollectionPipelineProcessor):
    seen = []

    def process(self, item):
        if item not in self.seen:
            self.receiver.send(item)
            self.seen.append(item)
