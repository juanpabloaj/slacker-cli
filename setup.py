#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def read(*paths):
    """ read files """
    with open(os.path.join(*paths), 'r') as filename:
        return filename.read()


install_requires = read('requirements.txt').splitlines()
try:
    import argparse
except ImportError:
    install_requires.append('argparse')


setup(
    name="slacker-cli",
    version="0.3.0",
    description="Send messages to slack from command line",
    long_description=(read('README.rst')),
    url="https://github.com/juanpabloaj/slacker-cli",
    install_requires=install_requires,
    license='MIT',
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    packages=['slacker_cli'],
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'slacker=slacker_cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)
