"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2
секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
Create the class - 'Traffic Light' and define a single color attribute and a method - 'running' . Implement
the attribute as private. As part of the method, implement switching traffic lights to the following modes:
red, yellow, green. The duration of the first state (red) is 7 seconds, the second (yellow) — 2 seconds, the
third (green) — as you wish. Switching between modes should only be performed in the specified order (red,
yellow, green). Test the example by creating an instance and calling the described method.
You can complicate the task by checking the order of modes, and if it is violated, output the corresponding
message and terminate the script.
"""


import time


class TrafficLight:
    def __init__(self, traffic_color):
        self.__color = traffic_color
        self

    def running(self):
        print(self.__color)


red = TrafficLight("red")
red.running()
time.sleep(7)
yellow = TrafficLight("yellow")
yellow.running()
time.sleep(2)
green = TrafficLight("green")
green.running()
time.sleep(7)
