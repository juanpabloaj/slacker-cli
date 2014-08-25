#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from mock import patch

from slacker_cli import post_message


class TestMessage(unittest.TestCase):

    @patch('slacker_cli.Slacker')
    def test_post_message_use_token(self, mock_slacker):
        token = 'aaa'
        channel = 'channel_name'
        message = 'message string'

        post_message(token, channel, message)

        mock_slacker.assert_called_with(token)
