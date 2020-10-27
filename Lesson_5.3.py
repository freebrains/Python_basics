"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Create a text file (without using a program), write down the names of employees and their
salaries line by line. Determine which employees have a salary of less than 20 thousand,
display the names of these employees.  Calculate average income of employees.
"""


n = 0  # количество строк
sum_income = []
with open(r"D:\Big_Data\Back_Up\Lesson_5.3.txt") as surname:
    for line in surname:
        n += 1
        new_list = line.split()
        sum_income.append(float(new_list[1]))
        if int(new_list[1]) < 20000:
            print(new_list[0], 'has salary less than 20000')
print("Average salary - ", sum(sum_income) / n)
