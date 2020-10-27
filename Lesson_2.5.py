"""
Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в
рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
Implement the 'Rating' structure, which is a non-increasing
set of natural numbers. You must request a new rating element
from the user. If there are elements with the same values
in the rating, then a new element with the same value should
be placed after them.
"""


m_list = [7, 5, 3, 3, 2]
y_number = int(input("Enter any number - "))
n = 0
for i in m_list:
    if y_number < i:
        n += 1
m_list.insert(n, float(y_number))
print(m_list)
