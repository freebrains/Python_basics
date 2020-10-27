"""
Представлен список чисел. Определить элементы списка, не имеющие
повторений. Сформировать итоговый массив чисел, соответствующих
требованию. Элементы вывести в порядке их следования в исходном
списке. Для выполнения задания обязательно использовать генератор.
A list of numbers is provided. Identify list items that do not have
repetitions. Generate a final array of numbers that match the
requirement. Display the items in the order they appear in the source
list. Use the generator to complete the task.
"""


m_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in m_list if m_list.count(i) < 2]

print(new_list)