"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20
или 21. Необходимо решить задание в одну строку.
For numbers between 20 and 240, find numbers that are
multiples of 20 or 21. You need to solve the task in one line.
"""


m_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(m_list)