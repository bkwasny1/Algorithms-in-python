#nieskonczone

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return f'{self.key}'


class Edge:
    def __init__(self, pojemnosc, resztowa):
        self.pojemnosc = pojemnosc
        self.resztowa = resztowa
        if resztowa is False:
            self.przeplyw_resztowy = pojemnosc
            self.flow = 0
        else:
            self.przeplyw_resztowy = 0
            self.flow = 0

    def __repr__(self):
        return f'{self.pojemnosc} {self.flow} {self.przeplyw_resztowy} {self.resztowa}'


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
        if idx1 == idx2:
            return None
        else:
            self.list[idx1].append((vertex2, edge))

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
            lista.append(self.getVertexIdx(i[0]))
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

    def BST(self, s=None):
        if s is None:
            s = self.vertex[0]
        visited = [False] * self.size
        parents = [-1 for _ in range(self.size)]
        queue = list()
        queue.append(s)
        idx = self.getVertexIdx(s)
        visited[idx] = True
        while queue:
            s = queue.pop()
            idx = self.getVertexIdx(s)
            for i in self.neighboursIdx(idx):
                if visited[i] is False:
                    vertex = self.getVertex(i)
                    for j in self.list[idx]:
                        if j[0] == vertex and j[1].przeplyw_resztowy > 0 and j[1].resztowa is False:
                            visited[i] = True
                            queue.append(self.vertex[i])
                            parents[i] = s
        return parents

    def analize(self, start_vertex, end_vertex, parents):
        idx = self.getVertexIdx(end_vertex)
        min_cap = float('inf')
        if isinstance(parents[idx], int):
            return 0
        else:
            start_idx = self.getVertexIdx(start_vertex)
            while idx != start_idx:
                par_idx = self.getVertexIdx(parents[idx])
                vertex = self.getVertex(idx)
                for j in self.list[par_idx]:
                    if j[0] == vertex and j[1].przeplyw_resztowy < min_cap:
                        min_cap = j[1].przeplyw_resztowy
                idx = par_idx
            return min_cap

    def augment(self, start_vertex, end_vertex, parents, min_cap):
        idx = self.getVertexIdx(end_vertex)
        start_idx = self.getVertexIdx(start_vertex)
        while idx != start_idx:
            par_idx = self.getVertexIdx(parents[idx])
            vertex = self.getVertex(idx)
            parent = parents[idx]
            for j in self.list[par_idx]:
                if j[0] == vertex and j[1].resztowa is False:
                    j[1].flow += min_cap
                    j[1].przeplyw_resztowy -= min_cap
            for i in self.list[idx]:
                if i[0] == parent and i[1].resztowa is True:
                    i[1].przeplyw_resztowy += min_cap

            idx = par_idx

    def Ford(self, start_vertex, end_vertex):
        parents = self.BST(start_vertex)
        min_cap = self.analize(start_vertex, end_vertex, parents)
        while min_cap > 0:
            self.augment(start_vertex, end_vertex, parents, min_cap)
            parents = self.BST(start_vertex)
            min_cap = self.analize(start_vertex, end_vertex, parents)

        przeplywy = 0
        neigh = self.neighboursIdx(self.getVertexIdx(end_vertex))
        for i in neigh:
            for j in self.list[i]:
                if j[0] == end_vertex:
                    przeplywy += j[1].flow
        return przeplywy


def main():
    graph = neighbourList()
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]

    for i in graf_0:
        graph.insertVertex(Vertex(i[0]))
        graph.insertVertex(Vertex(i[1]))
        graph.insertEdge(Vertex(i[0]), Vertex(i[1]), Edge(i[2], False))
        graph.insertEdge(Vertex(i[1]), Vertex(i[0]), Edge(i[2], True))
    print(graph.Ford(Vertex('s'), Vertex('t')))
    graph.printGraph()

main()


def main2():
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]

    graph = neighbourList()
    for i in graf_1:
        if i[0] == 'a' and i[1] == 'c':
            graph.insertVertex(Vertex(i[0]))
            graph.insertVertex(Vertex(i[1]))
            graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
        elif i[0] == 'c' and i[1] == 'a':
            graph.insertVertex(Vertex(i[0]))
            graph.insertVertex(Vertex(i[1]))
            graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
        else:
            graph.insertVertex(Vertex(i[0]))
            graph.insertVertex(Vertex(i[1]))
            graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
            graph.insertEdge(Vertex(i[1]), Vertex(i[0]), (Edge(i[2], True)))

    print(graph.Ford(Vertex('s'), Vertex('t')))
    graph.printGraph()

main2()


def main3():
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graph = neighbourList()
    for i in graf_2:
        graph.insertVertex(Vertex(i[0]))
        graph.insertVertex(Vertex(i[1]))
        graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
        graph.insertEdge(Vertex(i[1]), Vertex(i[0]), (Edge(i[2], True)))

    print(graph.Ford(Vertex('s'), Vertex('t')))
    graph.printGraph()

main3()


def main4():
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    graph = neighbourList()
    for i in graf_3:
        if i[0] == 'd' and i[1] == 'b':
            graph.insertVertex(Vertex(i[0]))
            graph.insertVertex(Vertex(i[1]))
            graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
        elif i[0] == 'b' and i[1] == 'd':
            graph.insertVertex(Vertex(i[0]))
            graph.insertVertex(Vertex(i[1]))
            graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
        else:
            graph.insertVertex(Vertex(i[0]))
            graph.insertVertex(Vertex(i[1]))
            graph.insertEdge(Vertex(i[0]), Vertex(i[1]), (Edge(i[2], False)))
            graph.insertEdge(Vertex(i[1]), Vertex(i[0]), (Edge(i[2], True)))

    print(graph.Ford(Vertex('s'), Vertex('t')))
    graph.printGraph()

main4()
