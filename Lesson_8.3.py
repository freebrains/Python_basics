"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Create your own exception class that should check the contents of the list for numbers only. Check the operation of
the exception on a real example. You must request data from the user and fill in the list. The exception class must
control the data types of list items.
Note: the length of the list is not fixed. Elements are requested indefinitely until the user stops the script by
entering, for example, the "stop" command. The script ends and the generated list is displayed on the screen.
"""


my_list = []
while True:
    try:
        new_value = input("Введите число или stop для остановки - ")
        if new_value == "stop":
            print(my_list)
            break
        else:
            list_value = int(new_value)
            my_list.append(list_value)
    except ValueError:
        print("Это не число")
