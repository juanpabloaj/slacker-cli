#!/usr/bin/python

import os

from setuptools import setup


def read(*paths):
    """read files"""
    with open(os.path.join(*paths)) as filename:
        return filename.read()


install_requires = read("requirements.txt").splitlines()


setup(
    name="slacker-cli",
    version="0.4.2",
    description="Send messages to slack from command line",
    long_description=(read("README.rst")),
    url="https://github.com/juanpabloaj/slacker-cli",
    install_requires=install_requires,
    license="MIT",
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    packages=["slacker_cli"],
    test_suite="tests",
    entry_points={"console_scripts": ["slacker=slacker_cli:main"]},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
