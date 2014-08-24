#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Send message to Slack from command line
"""

from slacker import Slacker
import argparse
import sys
import os


def post_message(token, channel, message):
    channel = '#{}'.format(channel)

    slack = Slacker(token)
    slack.chat.post_message(channel, message)


def args_priority(args, environ):
    '''
        priority of token
        1) as argumment: -t
        2) as environ variable
    '''

    arg_token = args.token

    slack_token_var_name = 'SLACK_TOKEN'
    if slack_token_var_name in environ.keys():
        token = environ[slack_token_var_name]
    else:
        token = None

    if arg_token:
        token = arg_token

    return token, args.channel


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--channel", help="Slack channel")
    parser.add_argument("-t", "--token", help="Slack token")

    args = parser.parse_args()

    token, channel = args_priority(args, os.environ)

    if not token or not channel:
        exit(1)

    message = sys.stdin

    post_message(token, channel, message)


if __name__ == '__main__':
    main()
