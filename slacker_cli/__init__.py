#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Send message to Slack from command line
"""

from slacker import Slacker
from slacker.utils import get_item_id_by_name
import requests
import argparse
import sys
import os
try:
    from urllib import quote as urllib_quote
except ImportError:
    from urllib.parse import quote as urllib_quote
import warnings
warnings.filterwarnings('ignore', message=".*InsecurePlatformWarning.*")


# This function will be removed after below PR is merged:
# https://github.com/os/slacker/pull/46
def get_item_by_key_value(list_dict, key, value):
    for d in list_dict:
        if d[key] == value:
            return d
    return {}


def post_message(token, channel, message, name, as_user, icon,
                 as_slackbot, team):
    if as_slackbot:
        post_message_as_slackbot(team, token, channel, message)
    else:
        slack = Slacker(token)
        slack.chat.post_message(channel, message, username=name,
                                as_user=as_user, icon_emoji=icon)


class SlackerCliError(Exception):
    pass


def post_message_as_slackbot(team, token, channel, message):
    url = 'https://{team}.slack.com/services/hooks/slackbot'
    url += '?token={token}&channel={channel}'
    url = url.format(team=team, token=token, channel=urllib_quote(channel))
    res = requests.post(url, message)
    if res.status_code != 200:
        raise SlackerCliError("{0}:'{1}'".format(res.content, url))


def get_im_id(token, username):
    slack = Slacker(token)
    members = slack.users.list().body['members']
    user_id = get_item_id_by_name(members, username)
    ims = slack.im.list().body['ims']
    return get_item_by_key_value(ims, key='user', value=user_id).get('id')


def get_channel_id(token, channel_name):
    slack = Slacker(token)
    channels = slack.channels.list().body['channels']
    return get_item_id_by_name(channels, channel_name)


def upload_file(token, channel_name, file_name):
    """ upload file to a channel """

    slack = Slacker(token)

    slack.files.upload(file_name, channels=channel_name)


def args_priority(args, environ):
    '''
        priority of token
        1) as argumment: -t
        2) as environ variable

        priority of as_user
        1) as argument: -a
        2) as environ variable
    '''

    arg_token = args.token
    arg_as_user = args.as_user

    slack_token_var_name = 'SLACK_TOKEN'
    if slack_token_var_name in environ.keys():
        token = environ[slack_token_var_name]
    else:
        token = None

    if arg_token:
        token = arg_token

    # slack as_user
    slack_as_user_var_name = 'SLACK_AS_USER'
    as_user = bool(environ.get(slack_as_user_var_name))

    if arg_as_user:
        as_user = True

    return token, as_user, args.channel


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--channel", help="Slack channel")
    parser.add_argument("-u", "--user", help="Slack user")
    parser.add_argument("-t", "--token", help="Slack token")
    parser.add_argument("-f", "--file", help="File to upload")
    parser.add_argument("-n", "--name", help="Sender name")
    parser.add_argument("-a", "--as-user", action="store_true", help="As user")
    parser.add_argument("-i", "--icon-emoji", help="Sender emoji icon")
    parser.add_argument("-s", "--as-slackbot", action="store_true",
                        help="Send as Slackbot")
    parser.add_argument("-m", "--team", help="Slack team")

    args = parser.parse_args()

    user = args.user
    message = sys.stdin.read()
    as_slackbot = args.as_slackbot
    if as_slackbot:
        token = args.token or os.environ.get('SLACKBOT_TOKEN')
        as_user = False
        channel = args.channel
        name = None
        icon = None
        file_name = None
        team = args.team or os.environ.get('SLACK_TEAM')
    else:
        token, as_user, channel = args_priority(args, os.environ)
        name = args.name
        icon = args.icon_emoji
        file_name = args.file
        team = None

    if token and channel and message:
        post_message(token, '#' + channel, message, name, as_user, icon,
                     as_slackbot, team)

    if token and user and message:
        if as_slackbot:
            channel = '@' + user
        else:
            im_id = get_im_id(token, user)
            channel = im_id or '@' + user  # allow user send DM to slackbot
        post_message(token, channel, message, name, as_user, icon,
                     as_slackbot, team)

    if token and file_name:
        if user:
            upload_file(token, '@' + user, file_name)
        elif channel:
            upload_file(token, '#' + channel, file_name)


if __name__ == '__main__':
    main()
