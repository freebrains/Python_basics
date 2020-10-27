"""
Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
Implement a script that should provide a function for calculating the
employee's salary. The calculation should use the formula:
(output in hours * rate per hour) + premium. To perform a calculation
for specific values, you need to run a script with parameters.
"""

from sys import argv

script_place, hours, rate, reward = argv
print("Место скрипта: ", script_place)
print("Выработка в часах: ", hours)
print("Ставка в час: ", rate)
print("Премия: ", reward)
print("Заработная плата: ", int(hours) * int(rate) + int(reward))
