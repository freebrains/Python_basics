"""
Программа принимает действительное положительное число x и
целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
The program takes a real positive number x and a negative
integer y. The number x must be raised to the power of y.
The task must be implemented as a function my_func(x, y).
Solve the task without the built - in function of exponentiation.
"""


def my_func(x=int(input("Введите основание - ")), y=int(input("Введите степень - "))):
    return x ** y


print(my_func())
