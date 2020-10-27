"""
 Реализовать формирование списка, используя функцию range() и
 возможности генератора. В список должны войти четные числа от
 100 до 1000 (включая границы). Необходимо получить результат
 вычисления произведения всех элементов списка.
 Implement the generation of a list using the range()
 function and capabilities of the generator. The list must include
 even numbers from 100 to 1000 (including borders). You need to
 get the result of calculating the product of all the elements
 in the list.
"""


from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


m_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(my_func, m_list))
