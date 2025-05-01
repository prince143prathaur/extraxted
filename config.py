#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8018549150:AAFI8u3S6BGvVfMxDgvkbOIYYttO7zBr6dM")
    API_ID = int(os.environ.get("API_ID", "21103196"))
    API_HASH = os.environ.get("API_HASH", "d0f94f6d2c3644e3e4e90d4b8be424ac")
    AUTH_USERS = "6473502061"
    LOG_CHAT_ID = int(os.environ.get("LOG_CHAT_ID", "6473502061"))

