#nieskonczone
import numpy as np
from copy import deepcopy

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

class neighbourMatrix:
    def __init__(self, init=0):
        self.size = 0
        self.init = init
        self.vertex = []
        self.matrix = []

    def isEmpty(self):
        if self.vertex is None:
            return True
        else:
            return False

    def insertVertex(self, vertex):
        if vertex not in self.vertex:
            self.vertex.append(vertex)
            self.size += 1
            for i in range(self.size - 1):
                self.matrix[i].append(self.init)
            self.matrix.append([self.init for i in range(self.size)])
        else:
            return None

    def insertEdge(self, vertex1, vertex2, edge=1):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if idx1 == idx2:
            return None
        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        for i in range(self.size):
            del self.matrix[i][idx]
        del self.matrix[idx]
        self.size -= 1
        self.vertex.remove(vertex)

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if idx1 == idx2:
            return None
        self.matrix[idx1][idx2] = self.init
        self.matrix[idx2][idx1] = self.init

    def getVertexIdx(self, vertex):
        return self.vertex.index(vertex)

    def getVertex(self, vertex_idx):
        return self.vertex[vertex_idx]

    def neighboursIdx(self, vertex_idx):
        lista = []
        for i in range(self.size):
            if self.matrix[vertex_idx][i] != self.init:
                lista.append(self.getVertexIdx(self.vertex[i]))
        return lista

    def edges(self):
        edge_list = []
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.init:
                    edge_list.append((self.vertex[i].key, self.vertex[j].key))
        return edge_list

    def order(self):
        if self.size == 0:
            return 0
        else:
            return len(self.vertex)

    def size_(self):
        if self.size == 0:
            return 0
        else:
            size = 0
            for i in range(self.size):
                for j in range(self.size):
                    if self.matrix[i][j] != self.init:
                        size = size + 1
            return int(size / 2)

    def __str__(self):
        matrix_string = ""
        for i in range(len(self.matrix)):
            matrix_string += f"{self.vertex[i].key} | "
            for j in range(len(self.matrix)):
                matrix_string += str(self.matrix[i][j]) + ' '
            matrix_string += '|\n'

        return matrix_string

    def vertex_deg(self, vertex_idx):
        deg = 0
        for i in self.matrix[vertex_idx]:
            if i != self.init:
                deg += 1
        return deg

    def ullman1(self, M_matrix, G, P, current_row=0, used_cols=None, no_recursion=0, izo_list=list()):
        no_recursion += 1
        x, y = M_matrix.shape
        if used_cols is None:
            used_cols = [False for _ in range(y)]
        if current_row == x:
            if (P == np.dot(M_matrix, np.transpose(np.dot(M_matrix, G)))).all():
                izo_list.append(deepcopy(M_matrix))
            return no_recursion, izo_list
        for i in range(y):
            if used_cols[i] is False:
                used_cols[i] = True
                for j in range(y):
                    if j == i:
                        M_matrix[current_row][j] = 1
                    else:
                        M_matrix[current_row][j] = 0
                no_recursion = self.ullman1(M_matrix, G, P, current_row + 1, used_cols, no_recursion)[0]
                used_cols[i] = False
        return no_recursion, izo_list

    def ullman2(self, M_matrix, G, P, M_zero, current_row=0, used_cols=None, no_recursion=0, izo_list=list()):
        no_recursion += 1
        x, y = M_matrix.shape
        if used_cols is None:
            used_cols = [False for _ in range(M_matrix.shape[1])]
        if current_row == x:
            if (P == np.dot(M_matrix, np.transpose(np.dot(M_matrix, G)))).all():
                izo_list.append(deepcopy(M_matrix))
            return no_recursion, izo_list
        for i in range(y):
            if used_cols[i] is False:
                if M_zero[current_row][i] == 1:
                    used_cols[i] = True
                    for j in range(y):
                        if j == i:
                            M_matrix[current_row][j] = 1
                        else:
                            M_matrix[current_row][j] = 0
                    no_recursion = self.ullman2(M_matrix, G, P, M_zero, current_row + 1, used_cols, no_recursion)[0]
                    used_cols[i] = False
        return no_recursion, izo_list

    def M_zero_matrix(self, G, P):
        M_zero = np.zeros((P.order(), G.order()))
        x, y = M_zero.shape
        for i in range(x):
            P_deg = P.vertex_deg(i)
            for j in range(y):
                G_deg = G.vertex_deg(j)
                if G_deg >= P_deg:
                    M_zero[i][j] = 1
        return M_zero

    def get_neighbours_numpy(self, array, idx):
        neigh = []
        count = 0
        for i in array[idx]:
            if i == 1:
                neigh.append(count)
            count += 1
        return neigh

    def prune(self, G, P, M):
        x, y = M.shape
        flag = False
        for i in range(x):
            for j in range(y):
                if M[i][j] == 1:
                    G_neigh = self.get_neighbours_numpy(G, j)
                    P_neigh = self.get_neighbours_numpy(P, i)
                    for x in P_neigh:
                        for y in G_neigh:
                            if M[x][y] == 1:
                                flag = True
                                break
                        if flag is False:
                            M[i][j] = 0
                            return False
        return True

    def ullman3(self, M_matrix, G, P, M_zero, current_row=0, used_cols=None, no_recursion=0, izo_list=list()):
        no_recursion += 1
        x, y = M_matrix.shape
        if used_cols is None:
            used_cols = [False for _ in range(M_matrix.shape[1])]
        if current_row == x:
            if (P == np.dot(M_matrix, np.transpose(np.dot(M_matrix, G)))).all():
                izo_list.append(deepcopy(M_matrix))
            return no_recursion, izo_list

        M = deepcopy(M_matrix)
        prune = True
        if current_row == x - 1:
            prune = self.prune(G, P, M)
        for i in range(y):
            if prune is False and current_row != 0:
                break
            if used_cols[i] is False:
                if M_zero[current_row][i] == 1:
                    used_cols[i] = True
                    for j in range(y):
                        if j == i:
                            M[current_row][j] = 1
                        else:
                            M[current_row][j] = 0
                    no_recursion = self.ullman3(M, G, P, M_zero, current_row + 1, used_cols, no_recursion)[0]

                    used_cols[i] = False
        return no_recursion, izo_list


def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    Matrix_G = neighbourMatrix()
    Matrix_P = neighbourMatrix()

    for i in graph_G:
        Matrix_G.insertVertex(Vertex(i[0]))
        Matrix_G.insertVertex(Vertex(i[1]))
        Matrix_G.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])


    for i in graph_P:
        Matrix_P.insertVertex(Vertex(i[0]))
        Matrix_P.insertVertex(Vertex(i[1]))
        Matrix_P.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])

    G_np = np.array(Matrix_G.matrix)
    P_np = np.array(Matrix_P.matrix)

    M = np.zeros((Matrix_P.order(), Matrix_G.order()))
    izo1 = Matrix_G.ullman1(M, G_np, P_np)
    print(len(izo1[1]), izo1[0])

    M = np.zeros((Matrix_P.order(), Matrix_G.order()))
    M_zero = Matrix_G.M_zero_matrix(Matrix_G, Matrix_P)
    izo2 = Matrix_G.ullman2(M, G_np, P_np, M_zero)
    print(len(izo2[1]), izo2[0])

    M = np.zeros((Matrix_P.order(), Matrix_G.order()))
    M_zero = Matrix_G.M_zero_matrix(Matrix_G, Matrix_P)
    izo3 = Matrix_G.ullman3(M, G_np, P_np, M_zero)
    print(len(izo3[1]), izo3[0])

main()
