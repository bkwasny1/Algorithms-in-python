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

    def chio(self):
        if self.size()[0] != self.size()[1]:
            return None
        if self.size()[0] == 2:
            det = self.A[0][0] * self.A[1][1] - self.A[0][1] * self.A[1][0]
            return det
        scalar = 1
        if self.A[0][0] == 0:
            for i in range(self.rows):
                if self.A[i][0] != 0:
                    self.A[0], self.A[i] = self.A[i], self.A[0]
                    scalar = -1
                    break
        B = Matrix((self.rows - 1, self.cols - 1))
        for i in range(B.size()[0]):
            for j in range(B.size()[1]):
                B[i][j] = Matrix([[self.A[0][0], self.A[0][j+1]],
                                [self.A[i+1][0], self.A[i+1][j+1]]])
                B[i][j] = B[i][j].chio()
        scalar *= self.A[0][0]**(self.rows-2)
        det = B.chio()
        return det / scalar


m1 = Matrix([
     [0, 1, 1, 2, 3],
     [4, 2, 1, 7, 3],
     [2, 1, 2, 4, 7],
     [9, 1, 0, 7, 0],
     [1, 4, 7, 2, 2]])

print(m1.chio())
