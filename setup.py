# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='RPSLS',
    version='0.1.0',
    description='Script that plays Rock-Paper-Scissors-Lizard-Spock. Multiple algorithms available.',
    long_description=readme,
    author='Juan Pablo Yamamoto',
    author_email='me@jpyamamoto.com',
    url='https://github.com/JPYamamoto/rpsls',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

