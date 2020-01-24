# -*-coding: utf8-*-
import argparse
import service

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string. 
# Sample String : `'w3resource'`
# Expected Result : `'w3ce'`
# Sample String : `'w3'`
# Expected Result : `'w3w3'`
# Sample String : `' w'`
# Expected Result : `Empty String`


interface = argparse.ArgumentParser(description=("Get a string made of the "
                                                 "first 2 and the last 2 chars from a given a string"))
interface.add_argument("text", help="any text", default="")


def main():
    args = interface.parse_args()
    print(service.cut_middle_chars(args.text))


if __name__ == '__main__':
    main()
