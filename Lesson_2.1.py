'''
Создать список и заполнить его элементами различных типов данных. Реализовать
скрипт проверки типа данных каждого элемента. Использовать функцию type()
для проверки типа. Элементы списка можно не запрашивать у пользователя, а
указать явно, в программе.
Create a list and fill it with elements of various data types.Implement a
script for checking the data type of each element. Use the type() function
in this script. You can specify the list items explicitly in the program
instead of requesting them from the user.
'''


m_list = [1, 1.23, "hello", {"whatsup?": 12, 25646: "fsfewdx", 1: False, 34342: None, }, (1, "во-первых", 2.12, "Yes")
          ]
for i in m_list:
    print(type(i))
