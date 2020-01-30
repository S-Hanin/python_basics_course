# -*-coding: utf8-*-
import service


# Write a Python script to merge two Python dictionaries


def main():
    a = {'a': 1}
    b = {'b': 2}
    print(f"merge of {a} and {b}: {service.merge_dicts(a, b)}")


if __name__ == '__main__':
    main()
