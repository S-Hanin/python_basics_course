# -*- coding: utf8 -*-

"""
Напишите шаблон регулярного выражения, который соответствовал
бы следующему формату времени:
`YYYY-MM-DDThh:mm:ss±hh:mm` (ISO формат).
"""
import re


def search_iso_date(text: str):
    """
    Search iso formatted (YYYY-MM-DDThh:mm:ss±hh:mm) date from text
    """

    pattern = r"""\d{4}-  # YYYY-
                  \d{2}-  # MM-
                  \d{2}T  # DDT
                  \d{2}:  # hh:
                  \d{2}:  # mm:
                  \d{2}[+-]  # ss[+-]
                  \d{2}:  # hh:
                  \d{2}   # mm"""
    match = re.search(pattern, text, re.VERBOSE)
    return match.group(0) if match else None


if __name__ == '__main__':
    TEXT = "today is 2005-08-09T18:31:42-03:30 and now we need to go another place"
    print(search_iso_date(TEXT))
