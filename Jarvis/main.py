#skończone
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'


class Points:
    def __init__(self, points_tab):
        self.tab = points_tab

    def find_min(self):
        min_y = 999999
        min_x = 999999
        for point in self.tab:
            if point.y < min_y:
                min_y = point.y
        points_min_y = list()
        for point in self.tab:
            if point.y == min_y:
                points_min_y.append(point)
        idx = 0
        for point in points_min_y:
            if point.x < min_x:
                min_x = point.x
                idx = points_min_y.index(point)
        return points_min_y[idx]

    def angle(self, p, q, r):
        angle = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
        return angle

    def distance(self, p1, p2):
        return np.sqrt((p1.y - p2.y)**2 + (p1.x - p2.x)**2)

    def Jarvis(self):
        start_point = self.find_min()
        p = start_point
        sheath = [start_point]
        while True:
            idx = self.tab.index(p) + 1
            if idx == len(self.tab):
                idx = 0
            q = self.tab[idx]
            for r in self.tab:
                angle = self.angle(p, q, r)
                if angle > 0:
                    q = r
            p = q
            if p == start_point:
                break
            sheath.append(q)
        return sheath

    def Jarvis2(self):
        start_point = self.find_min()
        p = start_point
        sheath = [start_point]
        while True:
            idx = self.tab.index(p) + 1
            if idx == len(self.tab):
                idx = 0
            q = self.tab[idx]
            for r in self.tab:
                angle = self.angle(p, q, r)
                if angle > 0:
                    q = r
                if angle == 0:
                    pq = self.distance(p, q)
                    rq = self.distance(r, q)
                    rp = self.distance(r, p)
                    max_distance = max(pq, rq, rp)
                    if max_distance == rp:
                        q = r
            p = q
            if p == start_point:
                break
            sheath.append(q)
        return sheath


def main():
    lista = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    tab = []
    for i in lista:
        tab.append(Point(i[0], i[1]))
    points = Points(tab)
    print(points.Jarvis())
    print(points.Jarvis2())


main()
