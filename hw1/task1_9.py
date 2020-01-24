# -*-coding: utf8-*-
import argparse
import service

# Write a Python program to remove duplicates from a list.


interface = argparse.ArgumentParser(description="Remove duplicates from a list")
interface.add_argument("text", help="any text or numbers with spaces", default="")


def main():
    args = interface.parse_args()
    print(service.remove_duplicates(args.text.split()))


if __name__ == '__main__':
    main()
