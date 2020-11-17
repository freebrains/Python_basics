"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина
* масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
Implement the class 'Road', which defines the attributes: length, width. The values of these attributes must be
defined when creating an instance of the class. Make the attributes protected. Determine the method for calculating
the mass of asphalt required to cover the entire roadway. Use the formula: length * width * mass of asphalt for
covering one square meter of road with asphalt, 1 cm thick * number of cm of roadbed thickness. Check how the method
works.
For example: 20 m * 5000 m * 25 kg * 5 cm = 12500 t
"""

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self, thickness=10, weight=20):
        calculation = thickness * weight * self._length * self._width
        return calculation


len_1 = Road(20, 5000)
print(len_1.calculate())
