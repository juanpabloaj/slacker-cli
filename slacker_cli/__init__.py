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


def get_channel_id(token, channel_name):
    slack = Slacker(token)
    channels = slack.channels.list().body['channels']
    for channel in channels:
        name, channel_id = channel['name'], channel['id']
        if name == channel_name:
            return channel_id


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
    parser.add_argument("-t", "--token", help="Slack token")
    parser.add_argument("-f", "--file", help="File to upload")

    args = parser.parse_args()

    token, channel = args_priority(args, os.environ)
    message = sys.stdin.read()
    file_name = args.file

    if token and channel and message:
        post_message(token, channel, message)

    if token and channel and file_name:
        upload_file(token, channel, file_name)


if __name__ == '__main__':
    main()
