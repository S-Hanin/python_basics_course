# -*-coding: utf8-*-
import argparse
import service

# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : `google.com`
# Expected Result : `{'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}`


interface = argparse.ArgumentParser(description="Count the number of characters")
interface.add_argument("text", help="any text", default="")


def main():
    args = interface.parse_args()
    print(service.count_frequency(args.text))


if __name__ == '__main__':
    main()
