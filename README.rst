===========
slacker-cli
===========

.. image:: https://travis-ci.org/juanpabloaj/slacker-cli.svg?branch=master
    :target: https://travis-ci.org/juanpabloaj/slacker-cli
.. image:: https://coveralls.io/repos/juanpabloaj/slacker-cli/badge.png?branch=master
    :target: https://coveralls.io/r/juanpabloaj/slacker-cli?branch=master


Send messages to `Slack <https://slack.com/>`_ from command line.

Usage
=====

::

    date | slacker -c slack_channel -t slack_token

Slack Token can be called from a enviroment variable, called ``SLACK_TOKEN``.

You can set ``SLACK_TOKEN`` in your ``~/.bashrc``

::

    # ~/.bashrc
    export SLACK_TOKEN="slack_token_string"

::

    date | slacker -c slack_channel

Upload file to channel::

    date | slacker -c slack_channel -f image.png

Installation
============

::

    pip install slacker-cli
