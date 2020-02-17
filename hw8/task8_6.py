# -*- coding: utf8 -*-
"""
Напишите шаблон регулярного выражения, который
соответствует вопросительным предложениям,
в которых одно слово (более 2 символов)
повторяется 4 или более раз.
"""
import re


def is_duplicated_words_in_question(text: str):
    """
    Checks sentence contains word duplicated four and more times
    Doesn't work with cyrillic
    """
    pattern = r".*(\w{2,})(.*?\1){3,}.*\?$"
    return bool(re.search(pattern, text))


if __name__ == '__main__':
    TEXT = "how much how to to to had you been saying and how" \
           " to speak so silly things like you?"
    print(TEXT)
    print(f"has duplicated words: {is_duplicated_words_in_question(TEXT)}")
