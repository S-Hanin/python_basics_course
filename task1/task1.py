# -*-coding: utf8-*-
from collections import Counter


# task1
def capitalize(text: str) -> str:
    return " ".join([word.capitalize() for word in text.split()])


# task2
def count_frequency(text: str) -> dict:
    return Counter(text)


# task3
def cut_middle_chars(text: str) -> str:
    if len(text) < 2:
        return ""
    return f"{text[:2]}{text[-2:]}"


# task4
def count_words(words: list) -> int:
    return len([word for word in words
                if len(word) > 2 and word.startswith(word[-1])])


# task5
def is_subset(first: set, second: set, third: set) -> bool:
    return third.issubset(first) and third.issubset(second)


# task6
def generate_squares(size: int) -> dict:
    return {x: x * x for x in range(1, size + 1)}


# task7
def merge_dicts(first: dict, second: dict) -> dict:
    result = {}
    result.update(first)
    result.update(second)
    return result


# task8
def get_highest_three_values(pairs: dict) -> list:
    if len(pairs) < 3:
        raise AssertionError("Dictionary must have 3 or more values")
    values = sorted(pairs.values())
    return values[-3:]


# task9
def remove_duplicates(collection: list) -> list:
    return list(set(collection))


# task10
def get_difference(first: list, second: list) -> list:
    collection = first + second
    return [item for item in collection if item not in first or item not in second]
