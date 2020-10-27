"""
Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего элемента.
A list of numbers is provided. You must output the elements of
the original list whose values are greater than the previous element.
"""


my_list = [300, 2, 12, 44, 11, 4, 10, 7, 1, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(new_list)
