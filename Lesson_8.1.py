"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
Implement the class - "date", whose constructor function must accept a date as a string in the "day-month-year" format.
Implement two methods within the class. The first, with the @classmethod decorator, should extract
the number, month, and year and convert their type to the "Number" type. The second one, with the @staticmethod
decorator, should validate the date, month, and year (for example, the month is from 1 to 12). Check the operation
of the resulting structure on real data.
"""


class Date:
    @classmethod
    def get_date(cls, date_param="01-12-2011"):
        return date_param.split("-")

    @staticmethod
    def control():
        print("Неверно введенная дата") if int(Date.get_date()[0]) > 31 or int(Date.get_date()[1]) > 12 \
            else print(f' День - {Date.get_date()[0]} \n Месяц - {Date.get_date()[1]} \n Год - {Date.get_date()[2]} ')




print(Date.control())

