class Matrix:
    def __init__(self, a, value=0):
        if isinstance(a, tuple):
            self.rows = a[0]
            self.cols = a[1]
            A = list()
            for i in range(self.rows):
                A.append([])
                for j in range(self.cols):
                    A[i].append(value)
            self.A = A
        else:
            self.A = a
            self.rows = len(a)
            self.cols = len(a[0])

    def __add__(self, other):
        if self.size() != other.size():
            return None
        else:
            B = Matrix((self.rows, self.cols))
            for i in range(self.rows):
                for j in range(self.cols):
                    B[i][j] = self.A[i][j] + other[i][j]
        return B

    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            return None
        B = Matrix((self.rows, other.size()[1]))
        for i in range(self.rows):
            for j in range(other.size()[1]):
                for k in range(other.size()[0]):
                    B[i][j] += self.A[i][k] * other[k][j]
        return B

    def __getitem__(self, item):
        return self.A[item]

    def __str__(self):
        matrix_string = ""
        for i in range(self.rows):
            matrix_string += "| "
            for j in range(self.cols):
                matrix_string += str(self.A[i][j]) + ' '
            matrix_string += '|\n'

        return matrix_string

    def size(self):
        return self.rows, self.cols


def matrix_transpose(matrix):
    B = Matrix((matrix.cols, matrix.rows))
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            B[j][i] = matrix[i][j]
    return B


m1 = Matrix([[1, 0, 2],
             [-1, 3, 1]])

m2 = Matrix((2, 3), 1)

m3 = Matrix([[3, 1],
             [2, 1],
             [1, 0]])

print(matrix_transpose(m1))
print(m1+m2)
print(m1*m3)
