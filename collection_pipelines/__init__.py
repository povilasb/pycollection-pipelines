from collection_pipelines.http import http
from collection_pipelines.json import json
from collection_pipelines.text import split, echo, cat, words, out
from collection_pipelines.std import value, head, tail, freq, count, filter, \
    unique

try:
    from collection_pipelines.graph import line, bar, wordcloud
except ImportError:
    pass
