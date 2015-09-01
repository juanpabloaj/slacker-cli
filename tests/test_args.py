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
        self.parser.as_user = 'arg_as_user'
        self.parser.channel = 'channel'
        args = self.parser
        environ = {'SLACK_TOKEN': 'env_token',
                   'SLACK_USERNAME': 'env_username'}

        self.assertEqual(
            ('arg_token', 'arg_as_user', 'channel'),
            args_priority(args, environ)
        )

    def test_args_priority_only_env_token(self):
        self.parser.token = None
        self.parser.as_user = None
        self.parser.channel = 'channel'
        args = self.parser
        environ = {'SLACK_TOKEN': 'env_token',
                   'SLACK_USERNAME': 'env_username'}

        self.assertEqual(
            ('env_token', 'env_username', 'channel'),
            args_priority(args, environ)
        )

    def test_args_priority_only_arg_token(self):
        self.parser.token = 'arg_token'
        self.parser.as_user = 'arg_username'
        self.parser.channel = 'channel'
        args = self.parser
        environ = {}

        self.assertEqual(
            ('arg_token', 'arg_username', 'channel'),
            args_priority(args, environ)
        )

    def test_args_priority_empty_args(self):
        self.parser.token = None
        self.parser.as_user = None
        self.parser.channel = None
        args = self.parser
        environ = {}

        self.assertEqual(
            (None, None, None),
            args_priority(args, environ)
        )
