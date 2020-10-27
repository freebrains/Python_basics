"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим
очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fibo_gen().
Функция отвечает за получение факториала числа, а в цикле необходимо
выводить только первые 15 чисел.
Implement the generator using a function with the yield keyword that creates
the next value. When calling the function, a generator object must be created.
The function should be called as follows: for el in fibo_gen(). The function
is responsible for getting the factorial of a number, and only the first 15
numbers must be output in the loop.
"""


from math import *
from itertools import count


def m_func():
    for i in count(1):
        yield factorial(i)


fact = m_func()
n = 0
for m in fact:
    if n == 15:
        break
    else:
        n += 1
        print(m)
