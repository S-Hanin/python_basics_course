# -*- coding: utf8 -*-

"""
Напишите шаблон регулярного выражения, который соответствовал бы паролю,
состоящему из 8-12 символов, среди которых могут быть строчные и заглавные
буквы латинского алфавита, цифры, нижнее подчеркивание, звездочка,
процент и амперсанд.
Пароль обязательно должен включать в себя одну строчную букву,
одну заглавную букву и одну цифру.
"""
import re


def search_iso_date(text: str):
    """
    Search iso formatted (YYYY-MM-DDThh:mm:ss±hh:mm) date from text
    """

    pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}"
    return re.match(pattern, text)


if __name__ == '__main__':
    TEXT = "today is 2005-08-09T18:31:42-03:30 and now we need to go another place"
    print(search_iso_date(TEXT))
