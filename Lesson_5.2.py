"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
Create a text file (without using a program), save several lines in it,
count the number of lines and the number of words in each line.
"""


with open(r"D:\Python_basics\Lesson_5.2.txt") as my_object:
    n = 0
    for line in my_object:
        n += 1
        print("Number of words in ", n, "line - ", line.count(' ') + 1)
print("Total number of lines - ", n)
