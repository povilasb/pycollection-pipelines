import functools


def coroutine(fn):
    def wrapper(*args, **kwargs):
        generator = fn(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


class CollectionPipelineProcessor:
    sink = None
    start_source = None
    receiver = None

    def process(self):
        raise NotImplementedError

    def on_done(self):
        if self.receiver:
            self.receiver.close()

    def source(self, start_source):
        self.start_source = start_source

    @coroutine
    def make_generator(self):
        while True:
            try:
                yield from self.process()
            except GeneratorExit:
                self.on_done()
                break

    def __or__(self, other):
        self.sink = other

        def exec():
            self.receiver = self.sink.make_generator()
            self.start_source()
        other.source(exec)

        return other
