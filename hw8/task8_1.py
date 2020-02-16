# -*- coding: utf8 -*-

"""
Напишите функцию, которая возвращает размер HTML документа
по адресу `https://google.com.`
Т.е. нужно получить страницу и вернуть ее размер (количество символов).
"""

import requests


def google_main_page_size():
    """
    Requests google main page and returns it's size
    """
    response = requests.get("https://google.com")
    if not response.ok:
        raise response.raise_for_status()
    return len(response.text)


if __name__ == '__main__':
    print(f"Google main page size: {google_main_page_size()}")
