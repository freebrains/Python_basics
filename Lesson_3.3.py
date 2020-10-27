"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
Implement the my_func () function, which takes three positional
arguments, and returns the sum of the largest two arguments.
"""


def my_func(var_1=int(input("Enter first number - ")), var_2=int(input("Enter second number - ")),
            var_3=int(input("Enter third number - "))):

    return sorted([var_1, var_2, var_3])[1:]


print(sum(my_func()))
