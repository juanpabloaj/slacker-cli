#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from mock import patch

from slacker_cli import get_channel_id, get_im_id, get_item_by_key_value


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

    @patch('slacker_cli.Slacker')
    def test_get_im_id(self, mock_slacker):

        mock_slacker.return_value.users.list.return_value.body = {
            'members': [
                {'name': 'bob', 'id': 'U111'},
                {'name': 'john', 'id': 'U222'}
            ]
        }
        mock_slacker.return_value.im.list.return_value.body = {
            'ims': [
                {'user': 'U111', 'id': 'IM111'},
                {'user': 'U111', 'id': 'IM222'}
            ]
        }

        self.assertEqual(
            'IM111', get_im_id('aaa', 'bob')
        )

    def test_get_item_by_key_value(self):
            list_dict = [{'user': 'user_id_1', 'id': '123'}, {}]

            self.assertEqual(
                '123',
                get_item_by_key_value(list_dict, 'user', 'user_id_1')['id'],
            )
