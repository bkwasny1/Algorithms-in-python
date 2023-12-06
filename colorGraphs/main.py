import polska

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
            matrix_string += "| "
            for j in range(len(self.matrix)):
                matrix_string += str(self.matrix[i][j]) + ' '
            matrix_string += '|\n'

        return matrix_string

    def colour(self, a=0, s=None):
        if s is None:
            s = self.vertex[0]
        colours = [i for i in range(self.size)]
        graph_colours = list()

        visited = [False] * self.size
        queue = list()
        queue.append(s)
        idx = self.getVertexIdx(s)
        visited[idx] = True
        while queue:
            s = queue.pop(a)
            available_colour = colours[:]
            for j in self.neighboursIdx(self.getVertexIdx(s)):
                vertex = self.getVertex(j)
                for i in graph_colours:
                    if i[0] == vertex.key and i[1] in available_colour:
                        available_colour.remove(i[1])
            graph_colours.append((s.key, min(available_colour)))
            for i in self.neighboursIdx(self.getVertexIdx(s)):
                if visited[i] is False:
                    queue.append(self.vertex[i])
                    visited[i] = True
        return graph_colours

class neighbourList:
    def __init__(self):
        self.size = 0
        self.vertex = []
        self.list = []

    def isEmpty(self):
        if self.vertex is None:
            return True
        else:
            return False

    def insertVertex(self, vertex):
        if vertex not in self.vertex:
            self.list.append([])
            self.vertex.append(vertex)
            self.size += 1
        else:
            return None

    def insertEdge(self, vertex1, vertex2, edge=1):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if idx1 == idx2 or vertex1 in self.list[idx2] or vertex2 in self.list[idx1]:
            return None
        else:
            self.list[idx1].append(vertex2)
            self.list[idx2].append(vertex1)

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        del self.list[idx]
        del self.vertex[idx]
        for i in self.list:
            if vertex in i:
                i.remove(vertex)
        self.size -= 1

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if idx1 == idx2:
            return None
        else:
            self.list[idx1].remove(vertex2)
            self.list[idx2].remove(vertex1)

    def neighboursIdx(self, vertex_idx):
        lista = []
        for i in self.list[vertex_idx]:
            lista.append(self.getVertexIdx(i))
        return lista

    def getVertexIdx(self, vertex):
        return self.vertex.index(vertex)

    def getVertex(self, vertex_idx):
        return self.vertex[vertex_idx]

    def edges(self):
        edge_list = []
        for i in range(self.size):
            for j in range(len(self.list[i])):
                if self.list[i] is not None:
                    edge_list.append((self.vertex[i].key, self.list[i][j].key))
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
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    size += 1
            return int(size / 2)

    def __str__(self):
        string = ''
        for i in self.list:
            string += '[ '
            for j in i:
                string += f"{j.key} "
            string += ' ]\n'
        return string

    def colour(self, a=0, s=None):
        if s is None:
            s = self.vertex[0]
        colours = [i for i in range(self.size)]
        graph_colours = list()

        visited = [False] * self.size
        queue = list()
        queue.append(s)
        idx = self.getVertexIdx(s)
        visited[idx] = True
        while queue:
            s = queue.pop(a)
            available_colour = colours[:]
            for j in self.neighboursIdx(self.getVertexIdx(s)):
                vertex = self.getVertex(j)
                for i in graph_colours:
                    if i[0] == vertex.key and i[1] in available_colour:
                        available_colour.remove(i[1])
            graph_colours.append((s.key, min(available_colour)))
            for i in self.neighboursIdx(self.getVertexIdx(s)):
                if visited[i] is False:
                    queue.append(self.vertex[i])
                    visited[i] = True
        return graph_colours


def main():
    pol = neighbourMatrix()
    #pol = neighbourList()
    for i in polska.graf:
        pol.insertVertex(Vertex(i[0]))
    for i in polska.graf:
        pol.insertEdge(Vertex(i[0]), Vertex(i[1]))

    pol.deleteVertex(Vertex('K'))
    pol.deleteEdge(Vertex('W'), Vertex('E'))

    #polska.draw_map(pol.edges(), pol.colour(0))   #DFS
    polska.draw_map(pol.edges(), pol.colour(-1))  #BFS

main()
