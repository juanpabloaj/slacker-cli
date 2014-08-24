#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Send message to Slack from command line
"""

from slacker import Slacker
import argparse
import sys


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--channel", help="Slack channel")
    parser.add_argument("-t", "--token", help="Slack token")

    args = parser.parse_args()
    token = args.token
    channel = '#{}'.format(args.channel)

    if not token or not channel:
        exit(1)

    message = sys.stdin

    slack = Slacker(token)

    slack.chat.post_message(channel, message)


if __name__ == '__main__':
    main()
