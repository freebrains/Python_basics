"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
Implement the base class - 'Car' . This class must have the following attributes: speed, color, name, is_police
(Boolean). And also methods: go, stop, turn(direction), which should report that the car went, stopped, turned
(where). Describe several child classes: Town Car, Sport Car, Work Car, Police Car. Add the show_speed method to the
base class, which should show the current speed of the car. For the Town Car and WorkCar classes, redefine the
show_speed method. If the speed value is greater than 60 (Town Car) and 40 (WorkCar), an 'Overspeed' message should
be displayed.
Create instances of classes and pass attribute values. Access the attributes and output the result. Call the methods
and also show the result.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.car_speed = speed
        self.car_color = color
        self.car_name = name
        self.car_is_police = is_police

    def go(self):
        print(self.car_name, "is moving")

    def stop(self):
        print(self.car_name, "is stopped")

    def turn_right(self):
        print(self.car_name, "is turning right")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(self.car_name, "is moving")

    def stop(self):
        print(self.car_name, "is stopped")

    def turn_right(self):
        print(self.car_name, "is turning right")

    def show_speed(self):
        print("Превышение скорости") if self.car_speed > 60 else print("Разрешенная скорость")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(self.car_name, "is moving")

    def stop(self):
        print(self.car_name, "is stopped")

    def turn_right(self):
        print(self.car_name, "is turning right")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(self.car_name, "is moving")

    def stop(self):
        print(self.car_name, "is stopped")

    def turn_right(self):
        print(self.car_name, "is turning right")

    def show_speed(self):
        print("Превышение скорости") if self.car_speed > 40 else print("Разрешенная скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(self.car_name, "is moving")

    def stop(self):
        print(self.car_name, "is stopped")

    def turn_right(self):
        print(self.car_name, "is turning right")


my_car = Car(40, "white", "Mazda", False)
my_car.go()
my_car.stop()
my_car.turn_right()
print()
my_town_car_1 = TownCar(80, "green", "Toyota", False)
my_town_car_1.go()
my_town_car_1.stop()
my_town_car_1.turn_right()
my_town_car_1.show_speed()
print()
my_town_car_2 = TownCar(55, "silver", "Nissan", False)
my_town_car_2.go()
my_town_car_2.stop()
my_town_car_2.turn_right()
my_town_car_2.show_speed()
print()
my_sport_car = SportCar(120, "red", "Porsche", False)
my_sport_car.go()
my_sport_car.stop()
my_sport_car.turn_right()
print()
my_work_car_1 = WorkCar(40, "white", "Volkswagen", False)
my_work_car_1.go()
my_work_car_1.stop()
my_work_car_1.turn_right()
my_work_car_1.show_speed()
print()
my_work_car_2 = WorkCar(55, "grey", "Skoda", False)
my_work_car_2.go()
my_work_car_2.stop()
my_work_car_2.turn_right()
my_work_car_2.show_speed()
