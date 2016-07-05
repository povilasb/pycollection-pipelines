import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

from wordcloud import WordCloud

from collection_pipelines.core import CollectionPipelineOutput


class GraphPipelineOutput(CollectionPipelineOutput):
    def __init__(self):
        self.x = []
        self.y = []

    def process(self, item):
        self.x.append(item[0])
        self.y.append(item[1])


class line(GraphPipelineOutput):
    """Displays pipeline data in a line chart."""
    def on_done(self):
        ax = plt.subplot(111)
        ax.plot(range(len(self.x)), self.y, marker='o')
        plt.yticks(range(len(self.y) + 1))
        plt.xticks(range(len(self.x) + 1), self.x, rotation='vertical')
        plt.show()


class bar(GraphPipelineOutput):
    """Displays pipeline data in a bar chart."""
    def on_done(self):
        ax = plt.subplot(111)
        ax.bar(range(len(self.x)), self.y, align='center')
        plt.yticks(range(len(self.y) + 1))
        plt.xticks(range(len(self.x) + 1), self.x, rotation='vertical')
        plt.show()


class wordcloud(CollectionPipelineOutput):
    """Draws wordcloud from the words in the pipeline."""
    def __init__(self) -> None:
        self.text = ''

    def process(self, item: str):
        self.text += item + ' '

    def on_done(self):
        wordcloud = WordCloud().generate(self.text)
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
