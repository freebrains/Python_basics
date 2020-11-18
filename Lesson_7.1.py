"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Implement the class - 'Matrix'. Provide an overload of the class constructor (the method 'init ()'), which must
accept data (a list of lists) to form a matrix.
The next step is to implement an overload of the method - 'str()' to output the matrix in the usual form.
Next, implement an overload of the method 'add()' to implement the operation of adding two objects of
the Matrix class (two matrices). The result of the addition should be a new matrix.
"""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.matrix)):
            sum_matrix.append([])
            for j in range(len(self.matrix[i])):
                sum_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return '\n'.join(map(str, sum_matrix))


my_matrix_1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
my_matrix_2 = Matrix([[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])
print(my_matrix_1 + my_matrix_2, )
