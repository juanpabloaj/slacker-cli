#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from mock import patch

from slacker_cli import post_message, SlackerCliError


class TestMessage(unittest.TestCase):

    @patch('slacker_cli.Slacker')
    def test_post_message_use_token(self, mock_slacker):
        token = 'aaa'
        channel = 'channel_name'
        message = 'message string'
        sender_name = None
        as_user = False
        sender_icon = None
        as_slackbot = False
        team = None

        post_message(token, channel, message,
                     sender_name, as_user, sender_icon,
                     as_slackbot, team)

        mock_slacker.assert_called_with(token)

    @patch('slacker_cli.Slacker')
    def test_post_message_use_channel_name(self, mock_slacker):
        token = 'aaa'
        channel = '#channel_name'
        message = 'message string'
        sender_name = None
        as_user = False
        sender_icon = None
        as_slackbot = False
        team = None

        post_message(token, channel, message,
                     sender_name, as_user, sender_icon,
                     as_slackbot, team)

        mock_slacker.return_value.chat.post_message\
            .assert_called_with('#channel_name', message,
                                username=None, as_user=False,
                                icon_emoji=None)

    @patch('slacker_cli.Slacker')
    def test_post_message_use_sender_name(self, mock_slacker):
        token = 'aaa'
        channel = '#channel_name'
        message = 'message string'
        sender_name = 'test bot'
        as_user = True
        sender_icon = ':dancer:'
        as_slackbot = False
        team = None

        post_message(token, channel, message,
                     sender_name, as_user, sender_icon,
                     as_slackbot, team)

        mock_slacker.return_value.chat.post_message\
            .assert_called_with('#channel_name', message,
                                username=sender_name, as_user=as_user,
                                icon_emoji=sender_icon)

    @patch('slacker_cli.requests')
    def test_post_message_as_slackbot(self, mock_requests):
        token = 'aaa'
        channel = '#channel_name'
        message = 'message string'
        sender_name = None
        as_user = False
        sender_icon = None
        as_slackbot = True
        team = 'team-name'

        try:
            post_message(token, channel, message,
                         sender_name, as_user, sender_icon,
                         as_slackbot, team)
        except SlackerCliError:
            pass

        url = 'https://team-name.slack.com/services/hooks/slackbot'
        url += '?token=aaa&channel=%23channel_name'
        mock_requests.post.assert_called_with(url, message)
