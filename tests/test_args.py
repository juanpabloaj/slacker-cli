#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
import argparse

from slacker_cli import args_priority


class TestArgs(TestCase):

    def setUp(self):
        self.parser = argparse.ArgumentParser()

    def test_args_priority_first_token_as_argument(self):
        self.parser.token = 'arg_token'
        self.parser.as_user = True
        self.parser.channel = 'channel'
        args = self.parser
        environ = {'SLACK_TOKEN': 'env_token',
                   'SLACK_AS_USER': 1}

        self.assertEqual(
            ('arg_token', True, 'channel'),
            args_priority(args, environ)
        )

    def test_args_priority_only_env_token(self):
        self.parser.token = None
        self.parser.as_user = False
        self.parser.channel = 'channel'
        args = self.parser
        environ = {'SLACK_TOKEN': 'env_token',
                   'SLACK_AS_USER': 1}

        self.assertEqual(
            ('env_token', 1, 'channel'),
            args_priority(args, environ)
        )

    def test_args_priority_only_arg_token(self):
        self.parser.token = 'arg_token'
        self.parser.as_user = True
        self.parser.channel = 'channel'
        args = self.parser
        environ = {}

        self.assertEqual(
            ('arg_token', True, 'channel'),
            args_priority(args, environ)
        )

    def test_args_priority_empty_args(self):
        self.parser.token = None
        self.parser.as_user = False
        self.parser.channel = None
        args = self.parser
        environ = {}

        self.assertEqual(
            (None, False, None),
            args_priority(args, environ)
        )
