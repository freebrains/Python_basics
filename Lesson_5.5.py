"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
Create (using a program) a text file and write (with a program) a set of numbers
separated  by spaces. The program must calculate the sum of the numbers in the
file and display it on the screen.
"""


number_sum = 0
with open(r"D:\Python_basics\Lesson_5.5.txt", 'w') as numbers:
    numbers.writelines(input("Enter numbers, using space - "))
with open(r"D:\Python_basics\Lesson_5.5.txt") as numbers:
    for line in numbers:
        numbers_list = line.split()
        for i in numbers_list:
            number_sum = number_sum + int(i)
    print(number_sum)
