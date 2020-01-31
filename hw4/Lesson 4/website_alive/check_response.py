# -*- coding: utf8 -*-

from make_request import request


def check_url(url: str) -> bool:
    return request(url).status_code == 200
