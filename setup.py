"""
Demo Python Flask app for running Python apps on Cloud Foundry
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cf-rps',
    version='1.0.0',
    description='Rock, Paper, Scissors game to demonstrate Cloud Foundry development concepts and service integrations.',
    long_description=description,
    url='https://github.com/solvaholic/cf-rps',
    license='Apache-2.0'
)
