#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "22877961 "))
    API_HASH = os.environ.get("API_HASH", "01b4a2f33d106880b4524073ef2242ea")
    AUTH_USERS = "1411895712"

