# -*- coding: utf8 -*-

"""
Напишите функцию, которая принимает три аргумента
  1)число, количество денег в исходной валюте, `float`;
  2)исходная валюта, трехсимвольная строка, `str`;
  3)целевая валюта, трехсимвольная строка, `str`;
  и возвращает количество денег в целевой валюте (тип `float`).
  Для получения курса валют воспользуйтесь `https://api.exchangerate-api.com`.
"""
import requests


def request_exchange_rates(currency_from):
    """
    Requests exchange rates for given currency
    from exchangerate-api.com

    :raises HTTPError
    :param currency_from:
    :return: dict
    """

    url = 'https://api.exchangerate-api.com/v4/latest/{}'
    response = requests.get(url.format(currency_from))
    if not response.ok:
        response.raise_for_status()
    data = response.json()
    return data.get("rates")


def convert_currency(money_quantity, currency_from, currency_to):
    """
    Converts money from one currency to other
    See currency codes at https://www.exchangerate-api.com/docs/supported-currencies

    :raises KeyError
    """
    coefficient = request_exchange_rates(currency_from).get(currency_to)
    if coefficient is None:
        raise KeyError("Unsupported currency code")
    return money_quantity * coefficient


if __name__ == '__main__':
    print(convert_currency(10, "USD", "RUB"))
