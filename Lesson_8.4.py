"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Start working on the "office equipment Warehouse" project. Create a class that describes the warehouse. As well as
the "office equipment" class, which will be the base class for successor classes. These classes are specific
types of office equipment (printer, scanner, copier). In the base class, define parameters that are common to the
given types. In the successor classes, implement parameters that are unique for each type of office equipment.
"""


data = []


class Orgtech:
    def __init__(self, weight, place, name, qty):
        self.weight = weight
        self.place = place
        self.name = name
        self.quantity = qty
        self.store_data()

    def store_data(self):
        data.append(self.__dict__)


class Printer(Orgtech):
    def __init__(self, weight, place, name, qty, print_time, form):
        super().__init__(weight, place, name, qty)
        self.time = print_time
        self.form = form


class Scanner(Orgtech):
    def __init__(self, weight, place, name, qty, scan_resolution, scan_color):
        super().__init__(weight, place, name, qty)
        self.resolution = scan_resolution
        self.color = scan_color


class Xerox(Orgtech):
    def __init__(self, weight, place, name, qty, speed, screen):
        super().__init__(weight, place, name, qty)
        self.speed = speed
        self.screen = screen


printer_1 = Printer(5, 'office', 'Canon 1060', 10, 2, 'A4')
printer_2 = Printer(10, 'library', 'Xerox 2000', 1, 1, 'A3')
scanner_1 = Scanner(6, 'office', 'Scanit 500', 15, 1080, 'color')
xerox_1 = Xerox(25, "account", "MFP Xerox", 4, 12, 'color')

print(data)
