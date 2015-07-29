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
        sender_name = None
        sender_icon = None

        post_message(token, channel, message, sender_name, sender_icon)

        mock_slacker.assert_called_with(token)

    @patch('slacker_cli.Slacker')
    def test_post_message_use_channel_name(self, mock_slacker):
        token = 'aaa'
        channel = '#channel_name'
        message = 'message string'
        sender_name = None
        sender_icon = None

        post_message(token, channel, message, sender_name, sender_icon)

        mock_slacker.return_value.chat.post_message\
            .assert_called_with('#channel_name', message,
                                username=None, icon_emoji=None)

    @patch('slacker_cli.Slacker')
    def test_post_message_use_sender_name(self, mock_slacker):
        token = 'aaa'
        channel = '#channel_name'
        message = 'message string'
        sender_name = 'test bot'
        sender_icon = ':dancer:'

        post_message(token, channel, message, sender_name, sender_icon)

        mock_slacker.return_value.chat.post_message\
            .assert_called_with('#channel_name', message,
                                username=sender_name, icon_emoji=sender_icon)
