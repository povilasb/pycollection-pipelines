from setuptools import setup

setup(
    name='collection-pipelines',
    version='0.1.3',
    description='Framework to implement collection pipelines in python.',
    long_description=open('README.rst').read(),
    url='https://github.com/povilasb/pycollection-pipelines',
    author='Povilas Balciunas',
    author_email='balciunas90@gmail.com',
    license='MIT',
    packages=['collection_pipelines'],
    install_requires=['typing==3.5.2.2'],
)
