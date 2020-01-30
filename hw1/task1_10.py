# -*-coding: utf8-*-
import service

# Get the difference between the two lists


def main():
    print("Program to get the difference between the two lists")
    first = input("enter first list: ").split()
    second = input("enter second list: ").split()
    print(service.get_difference(first, second))


if __name__ == '__main__':
    main()
