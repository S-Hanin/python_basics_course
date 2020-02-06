# -*- coding: utf8 -*-

"""
Разработать класс `Complex`, которые бы описывал комплексные
числа, позволял их складывать, вычитать, умножать, делить и получать модуль.
Вывод действительной и мнимой частей должен быть с точностью
до двух знаков после запятой.

На вход:
действительная и мнимая часть числа, разделенная пробелом.

На выходе:
Для двух комплексных чисел вывод должен быть в следующей последовательности
в отдельных строках:
`C + D`
`C – D`
`C * D`
`C/D`
`mod(C)`
`mod(D)`

P.S. Не забудьте про перегрузку магических методов, пожалуйста
"""
import math
import operator


class Complex:
    """
    Complex number simple representation
    """
    def __init__(self, complex_str: str):
        self.real, self.imag = map(float, complex_str.split())

    @classmethod
    def build(cls, real, imag):
        """
        Creates new Complex instance
        """
        return cls(f"{real} {imag}")

    def __str__(self):
        return f"{self.real:.2f}{self.imag:+.2f}j"

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return self.build(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return self.build(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return self.build(real, imag)

    def __truediv__(self, other):
        real = ((self.real * other.real + self.imag * other.imag)
                / (other.real ** 2 + other.imag ** 2))
        imag = ((other.real * self.imag - self.real * other.imag)
                / (other.real ** 2 + other.imag ** 2))
        return self.build(real, imag)

    def __abs__(self):
        return round(math.sqrt(self.real ** 2 + self.imag ** 2), 2)


def main():
    """
    Class Complex at work
    :return:
    """
    c_num = Complex("3 2")
    d_num = Complex("-4 2")
    operations = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul,
                  "/": operator.truediv}
    print(f"C = {c_num}, D = {d_num}")
    for op_sign, operation in operations.items():
        print(f"C {op_sign} D = {operation(c_num, d_num)}")
    print(f"mod(C) = {abs(c_num)}")
    print(f"mod(D) = {abs(d_num)}")


if __name__ == '__main__':
    main()
