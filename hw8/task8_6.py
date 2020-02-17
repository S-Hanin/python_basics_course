# -*- coding: utf8 -*-
"""
Напишите шаблон регулярного выражения, который
соответствует вопросительным предложениям,
в которых одно слово (более 2 символов)
повторяется 4 или более раз.
"""
import re


def is_queston_has_duplicated_words(text: str):
    """
    Checks sentence contains word duplicated four and more times
    Doesn't work with cyrillic
    """
    rx = r".*(\w{2,})(.*?\1){3,}.*\?$"
    return True if re.search(rx, text) else False


if __name__ == '__main__':
    TEXT = "how much how to to to had you been saying and how" \
           " to speak so silly things like you?"
    print(TEXT)
    print(f"has duplicated words: {is_queston_has_duplicated_words(TEXT)}")
