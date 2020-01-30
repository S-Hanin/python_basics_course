# -*-coding: utf8-*-
import service


# Write a Python script to generate and print a dictionary that contains
# a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`


def main():
    print(f"{service.generate_squares(5)}")


if __name__ == '__main__':
    main()
