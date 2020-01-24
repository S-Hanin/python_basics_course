# -*-coding: utf8-*-
import argparse
import service

# Write a Python program to count the number of strings where the string length is 2 or more and the
# first and last character are same from a given list of strings. 
# Sample List : `['abc', 'xyz', 'aba', '1221']`
# Expected Result : `2`


interface = argparse.ArgumentParser(description=("Count the number of strings where the string length is 2 or more"
                                                 " and the first and last character are same"))
interface.add_argument("text", help="any text with spaces", default="")


def main():
    args = interface.parse_args()
    print(service.count_words(args.text.split()))


if __name__ == '__main__':
    main()
