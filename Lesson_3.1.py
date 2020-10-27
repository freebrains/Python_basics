"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
Implement a function that uses two numbers (positional arguments)
and divides them. Request the numbers from the user, consider
handling the situation of division by zero.
"""


def m_func(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        print("Can't divide by 0. Try not 0 value")
        return


print(m_func(float(input("Enter first number - ")), float(input("Enter second number - "))))
