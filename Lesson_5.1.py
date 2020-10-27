"""
 Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
 Create with a program file in text format and write the data entered by the user line
 by line. An empty string indicates the end of data entry.
"""


first_task = open("lesson_5.txt", 'a')
first_task.write(input("Enter a word -  ") + "\n")
first_task.close()
