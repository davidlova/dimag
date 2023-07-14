#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6396515718:AAEPHBJ0g6Wbu6G0_cO9tKtVrntUaJhomO0")
    API_ID = int(os.environ.get("API_ID", "8405475"))
    API_HASH = os.environ.get("API_HASH", "2575cc32b15cc2002fc1903324217d62")
    AUTH_USERS = "108380022"

