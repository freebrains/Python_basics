"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
Implement the project for the calculation of total fabric consumption for the garment industry. The main entity
(class) of this project is clothing, which can have a specific name. The types of clothing in this project include
coats and suits. These types of clothing options are available: size (for coat) and growth (for a suit). These can
be ordinary numbers: V and H, respectively.
To determine the fabric consumption for each type of clothing, use the formulas: for coats (V/6.5 + 0.5),
for suits (2 * H + 0.3). Test how these methods work on real data.
Implement a calculation of fabric consumption. Test the knowledge gained in this lesson: implement abstract classes
for the main project classes, and test the @property decorator in practice.
"""

from abc import abstractmethod


class Clothes:
    @abstractmethod
    def fabric(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def fabric(self):
        return self.height * 2 + 0.3


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def fabric(self):
        return self.size / 6.5 + 0.5


my_suit = Suit(1.85)
print(my_suit.fabric())
my_coat = Coat(52)
print(my_coat.fabric())
