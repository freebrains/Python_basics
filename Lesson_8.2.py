"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
Create your own exception class that handles the division-by-zero situation. Check its operation on the data entered
by the user. If the user enters zero as a divisor, the program must correctly handle this situation and not fail.
"""


class MyError(Exception):
    def __init__(self, t="На ноль делить нельзя"):
        self.text = t


denomitor = int(input("Введите знаменатель - "))
dividend = int(input("Введите делитель - "))
try:
    print(dividend / denomitor)
    if denomitor == 0:
        raise MyError
except ZeroDivisionError:
    print("На ноль делить нельзя")
