#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Send message to Slack from command line
"""

from slacker import Slacker
from slacker.utils import get_item_id_by_name
import argparse
import sys
import os
import warnings
warnings.filterwarnings('ignore', message=".*InsecurePlatformWarning.*")


def post_message(token, channel, message, name, icon):
    slack = Slacker(token)
    slack.chat.post_message(channel, message, username=name, icon_emoji=icon)


def get_channel_id(token, channel_name):
    slack = Slacker(token)
    channels = slack.channels.list().body['channels']
    return get_item_id_by_name(channels, channel_name)


def upload_file(token, channel, file_name):
    """ upload file to a channel """

    slack = Slacker(token)
    channel_id = get_channel_id(token, channel)

    slack.files.upload(file_name, channels=channel_id)


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
    parser.add_argument("-u", "--user", help="Slack user")
    parser.add_argument("-t", "--token", help="Slack token")
    parser.add_argument("-f", "--file", help="File to upload")
    parser.add_argument("-n", "--name", help="Sender name")
    parser.add_argument("-i", "--icon-emoji", help="Sender emoji icon")

    args = parser.parse_args()

    token, channel = args_priority(args, os.environ)
    user = args.user
    name = args.name
    icon = args.icon_emoji
    message = sys.stdin.read()
    file_name = args.file

    if token and channel and message:
        post_message(token, '#' + channel, message, name, icon)

    if token and user and message:
        post_message(token, '@' + user, message, name, icon)

    if token and channel and file_name:
        upload_file(token, channel, file_name)


if __name__ == '__main__':
    main()
