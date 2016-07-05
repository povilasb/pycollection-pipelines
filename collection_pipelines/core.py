import functools
from typing import Callable


def coroutine(fn: Callable):
    def wrapper(*args, **kwargs):
        generator = fn(*args, **kwargs)
        next(generator)
        return generator

    return wrapper


class CollectionPipelineProcessor:
    sink = None
    start_source = None
    receiver = None

    def process(self, item):
        raise NotImplementedError

    def on_done(self):
        if self.receiver:
            self.receiver.close()

    def source(self, start_source):
        self.start_source = start_source

    def return_value(self):
        """Processor return value when used with __or__ operator.

        Returns:
            CollectionPipelineProcessor: when processor is to be chained
                with other processors.
            any: any other value when processor is used as an output and is
                meant to return value. In this way we can assign
                the output result to python variable.
        """
        return self

    @coroutine
    def make_generator(self):
        while True:
            try:
                item = yield
                self.process(item)
            except GeneratorExit:
                self.on_done()
                break

    def __or__(self, other):
        """Overwrites the '|' operator.

        Args:
            other (CollectionPipelineProcessor)

        Returns:
            whatever other.return_value() returns.
        """
        self.sink = other

        def exec():
            self.receiver = self.sink.make_generator()
            self.start_source()
        other.source(exec)

        return other.return_value()


class CollectionPipelineOutput(CollectionPipelineProcessor):
    """Pipeline processor that ends the chain and starts outputing stream.

    Output processor immediately starts consuming from the source.
    Thus triggering the whole pipeline start.
    """
    def source(self, start_source: CollectionPipelineProcessor):
        start_source()

    def return_value(self) -> None:
        return None


class CollectionPipelineSource(CollectionPipelineProcessor):
    """Pipeline data source processor."""
    def __init__(self):
        self.source(self.on_begin)

    def on_begin(self):
        """Constructs the items generator."""
        raise NotImplementedError
