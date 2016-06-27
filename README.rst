=====
About
=====

Experimental `collection pipeline <http://martinfowler.com/articles/collection-pipeline/>`_
pattern implementation in python.

.. code-block:: python

    cat('/tmp/file.txt') | filter('some line') | filter('some line 2') | out()
