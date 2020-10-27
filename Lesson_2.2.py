"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном
количестве элементов последний сохранить на своем месте. Для заполнения
списка элементов необходимо использовать функцию input().
For a list, implement the exchange of values of neighboring elements, i.e.
the values are exchanged for elements with indexes 0 and 1, 2 and 3 etc.
If the number of elements is odd, keep the last one on its place. To fill
the list of elements, use the input() function
"""

m_list = [1, 45, 76, "HI", 34]
y_list = list(input("Enter anything and I will change it - "))
for i in range(1, len(y_list), 2):
    y_list[i - 1], y_list[i] = y_list[i], y_list[i - 1]
print(y_list)
