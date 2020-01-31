# -*- coding: utf8 -*-

import requests


def request(url: str):
    return requests.get(url)
