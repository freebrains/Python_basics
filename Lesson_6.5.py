"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
(карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
Implement the class 'Stationery'. Define the attribute - 'title' and the method - 'draw' in it. The method displays
the message "Starting rendering". Create three child classes 'Pen', 'Pencil', and 'Handle'. Implement an override
of the method 'draw' in each of the classes. For each class, the method must output a unique message. Create instances
of classes and check what the described method outputs for each instance.
"""

class Stationery:
    def __init__(self, title):
        self.name = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


pen = Pen("Ручка")
pen.draw()
print()
pencil = Pencil("Карандаш")
pencil.draw()
print()
ha = Handle("Маркер")
ha.draw()
