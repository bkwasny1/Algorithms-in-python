#skonczone
import graf_mst


class Vertex:
    def __init__(self, key, colour=None):
        self.key = key
        self.colour = colour

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


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
        for i in self.list[idx1]:
            if i[0] == vertex2:
                return None
        for i in self.list[idx2]:
            if i[0] == vertex1:
                return None
        if idx1 == idx2:
            return None
        else:
            self.list[idx1].append((vertex2, edge))
            self.list[idx2].append((vertex1, edge))

    def deleteVertex(self, vertex):
        idx = self.getVertexIdx(vertex)
        del self.list[idx]
        del self.vertex[idx]
        for i in self.list:
            for j in range(len(i)):
                if i[j][0] == vertex:
                    del i[j]
                    break
        self.size -= 1

    def deleteEdge(self, vertex1, vertex2):
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        if idx1 == idx2:
            return None
        else:
            for i in self.list[idx1]:
                if i[0] == vertex2:
                    self.list[idx1].remove(i)
            for i in self.list[idx2]:
                if i[0] == vertex1:
                    self.list[idx2].remove(i)

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
                    edge_list.append((self.vertex[i].key, self.list[i][j][0].key))
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
                string += f"{j[0].key}:{j[1]} "
            string += ' ]\n'
        return string

    def printGraph(self):
        n = self.order()
        print("------GRAPH------", n)
        for i in range(n):
            v = self.getVertex(i)
            print(v.key, end=" -> ")
            nbrs = self.list[i]
            for (j, w) in nbrs:
                print(j.key, w, end=";")
            print()
        print("-------------------")

    def find_min(self, vertex, lista):
        v = self.getVertexIdx(vertex)
        min_ = 0, 99999999
        prev = v
        for j in lista:
            c = self.getVertexIdx(j)
            for i in self.list[c]:
                if i[1] < min_[1] and i[0] not in lista:
                    min_ = i[0], i[1]
                    prev = c
        if min_[1] == 99999999:
            return v, 99999999, 'end'
        return self.getVertexIdx(min_[0]), min_[1], prev

    def prim(self, vertex):
        tree = neighbourList()
        intree = [0 for _ in range(self.size)]
        distance = [99999999 for _ in range(self.size)]
        parent = [-1 for _ in range(self.size)]
        v = self.getVertexIdx(vertex)
        tree.insertVertex(vertex)

        while 0 in intree:
            intree[v] = 1
            idx, min_, prev = self.find_min(self.getVertex(v), tree.vertex)
            if min_ < distance[v] and intree[idx] == 0:
                distance[v] = min_
                parent[idx] = v
            tree.insertVertex(self.getVertex(idx))
            if prev == 'end':
                break
            tree.insertEdge(self.getVertex(prev), self.getVertex(idx), min_)
            v = idx
        return tree


def main():
    graph = neighbourList()
    for i in graf_mst.graf:
        graph.insertVertex(Vertex(i[0]))
        graph.insertVertex(Vertex(i[1]))
    for i in graf_mst.graf:
        graph.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
    tree = graph.prim(Vertex('A'))
    tree.printGraph()


main()
