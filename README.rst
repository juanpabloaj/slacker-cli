===========
slacker-cli
===========

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

Installation
============

::

    pip install slacker-cli
