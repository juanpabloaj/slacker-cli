===========
slacker-cli
===========

.. image:: https://travis-ci.org/juanpabloaj/slacker-cli.svg?branch=master
    :target: https://travis-ci.org/juanpabloaj/slacker-cli
.. image:: https://coveralls.io/repos/juanpabloaj/slacker-cli/badge.svg?branch=master
    :target: https://coveralls.io/r/juanpabloaj/slacker-cli?branch=master

Send messages to `Slack <https://slack.com/>`_ from command line.

Usage
=====

.. code-block:: bash

    date | slacker -c slack_channel -t slack_token

The `Slack token <https://api.slack.com/web#authentication>`_ can be called from an enviroment variable, called ``SLACK_TOKEN``.

You can set ``SLACK_TOKEN`` in your ``~/.bashrc``

.. code-block:: bash

    # ~/.bashrc
    export SLACK_TOKEN="slack_token_string"

.. code-block:: bash

    date | slacker -c slack_channel

Send message to user:

.. code-block:: bash

    date | slacker -u user_name

Upload file to channel:

.. code-block:: bash

    date | slacker -c slack_channel -f image.png

Add sender name and emoji avatar:

.. code-block:: bash

    date | slacker -n SlackerBot -i :dancer:

Installation
============

.. code-block:: bash

    pip install slacker-cli

Tokens
======

You can either `generate test tokens <https://api.slack.com/docs/oauth-test-tokens>`_ or  `create a bot user and use its token <https://my.slack.com/apps/A0F7YS25R-bots>`_.

Contributors
============

- `Alex Jurkiewicz <https://github.com/alexjurkiewicz>`_
- `David Yen <https://github.com/davidyen1124>`_
- `Ethan Erchinger <https://github.com/erchn>`_
- `Hugo van Kemenade <https://github.com/hugovk>`_
- `JuanPablo AJ <https://github.com/juanpabloaj>`_
- `Kentaro Wada <https://github.com/wkentaro>`_
- `Marc Abramowitz <https://github.com/msabramo>`_
- `Valentin Lab <https://github.com/vaab>`_
