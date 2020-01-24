# -*-coding: utf8-*-
import argparse
import service

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalized correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.
# Input Format: `A single line of input containing the full name, S.`
# Constraints: `0 < len(S) < 1000`
# The string consists of alphanumeric characters and spaces.
# Note: `in a word only the first character is capitalized.`
# Example: `12abc when capitalized remains 12abc.`
# Output Format: `Print the capitalized string, S.`


interface = argparse.ArgumentParser(description=("Ensure that the first and last names of "
                                                 "people begin with a capital letter"))
interface.add_argument("name", help="Name Surname", default="")


def main():
    args = interface.parse_args()
    print(service.capitalize(args.name))


if __name__ == '__main__':
    main()
