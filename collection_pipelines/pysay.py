from collection_pipelines.core import CollectionPipelineOutput


TEMPLATE = """
{}
    \\
     \\
         .-----.
        | O     |
        +---.   |
        ____|   |
      +         . .--.
     |   .-----+  |   |
     |   | .-----+    |
      +-+ /    ______.+
          |   |
          |   +---.
          \     O |
           +-----+
"""

def make_text_box(text: str) -> str:
    """Frames the specified text."""
    return '  {}\n< {} >\n  {}'.format('_' * len(text), text, '-' * len(text))


class pysay(CollectionPipelineOutput):
    """Prints incoming text items as python talk bubbles."""

    def process(self, item: str) -> None:
        print(TEMPLATE.format(make_text_box(item)))
