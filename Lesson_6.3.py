"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать
данные, проверить значения атрибутов, вызвать методы экземпляров).
Implement the base class - 'Worker', which defines the attributes: name, surname, position, income. The last
attribute must be protected and refer to a dictionary containing the elements: salary and bonus, for example,
{"wage": wage, "bonus": bonus}. Create the class - 'Position'  based on the class 'Worker'. In the class
'Position', implement methods for getting the full name of the employee (get_full_name) and income with bonus
(get_total_income). Check how the example works on real data (create instances of the class 'Position', pass the
data, check attribute values, and call instance methods).
"""


class Worker:
    def __init__(self, name, surname, position, wages, bonus):
        self.worker_name = name
        self.worker_surname = surname
        self.worker_position = position
        self._income = {"wages": wages, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.worker_name, self.worker_surname)

    def get_total_income(self):
        print(sum(self._income.values()))


new_worker = Position("Alex", "Baranov", "Product specialist", 50000, 120000)
new_worker.get_full_name()
new_worker.get_total_income()
print(new_worker.worker_position)
