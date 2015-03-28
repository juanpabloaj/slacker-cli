#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from mock import patch

from slacker_cli import get_channel_id


class TestChannels(unittest.TestCase):

    @patch('slacker_cli.Slacker')
    def test_get_channel_id(self, mock_slacker):

        mock_slacker.return_value.channels.list.return_value.body = {
            'channels': [
                {'name': 'general', 'id': 'C111'},
                {'name': 'random', 'id': 'C222'}
            ]
        }

        self.assertEqual(
            'C111', get_channel_id('aaa', 'general')
        )
