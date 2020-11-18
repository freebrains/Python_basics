"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до
целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу. Если
ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: **\n\n***.
Implement a program for working with organic cells. You must create the class - 'Cell'. In its constructor,
initialize the parameter corresponding to the number of cells (an integer). The class must implement methods for
overloading arithmetic operators: addition (add ()), subtraction (sub ()), multiplication (mul ()),
division (truediv ()). These methods should only be applied to cells and perform increment, decrement, multiplication,
and normal (non-integer) cell division, respectively. In the method of division should be rounding values to the
nearest whole number.
Addition. The Union of two cells. In this case, the number of cells in the common cell must be equal to the sum of
the cells of the original two cells.
Subtraction. Two cells are involved. The operation must be performed only if the difference in the number of cells
of two cells is greater than zero, otherwise the corresponding message is displayed.
Multiplication. A shared cell of two is created. The number of cells in a common cell is defined as the product of
the number of cells in these two cells.
Division. A shared cell of two is created. The number of cells in a shared cell is defined as the integer division
of the number of cells in these two cells.
The class must implement the method - 'make_order ()' , which accepts an instance of the class and the number of cells
in the row. This method allows you to organize cells in rows.
The method should return a string of the form **\n\n***..., where the number of cells between \n is equal to the
passed argument. If there are not enough cells to form a row, then all the remaining cells are written to the last row.
For example, the number of cells in a cell is 12, and the number of cells in a row is 5. Then the make_order() method
returns the string: **\n\n.
Or the number of cells in a cell is 15, and the number of cells in a row is 5.then the make_order() method returns
the string: **\n\n***.
"""


class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def make_order(self, row):
        for i in range(self.cell_number // row):
            c = "*" * row
            print(c)
        print("*" * int(self.cell_number % row))

    def __add__(self, other):
        return self.cell_number + other.cell_number

    def __sub__(self, other):
        return self.cell_number - other.cell_number if self.cell_number - other.cell_number > 0 else \
            print("Error. Cell number can't be < 0")

    def __mul__(self, other):
        return self.cell_number * other.cell_number

    def __truediv__(self, other):
        return self.cell_number // other.cell_number


cell_1 = Cell(7)
cell_2 = Cell(15)
print(cell_2.make_order(4))
