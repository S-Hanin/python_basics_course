# -*-coding: utf8-*-
import service


# Write a Python program to find the highest 3 values in a dictionary


def main():
    test_data = service.generate_squares(5)
    print(f"3 highest values of {test_data}: {service.get_highest_three_values(test_data)}")


if __name__ == '__main__':
    main()
