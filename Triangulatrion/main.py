#nieskonczone
import numpy as np
import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x},{self.y})'


def distance(p1, p2):
    return np.sqrt((p1.y - p2.y) ** 2 + (p1.x - p2.x) ** 2)


def triangle_cost(a, b, c):
    ab = distance(a, b)
    ac = distance(a, c)
    cb = distance(c, b)
    return ab + ac + cb


def minCost_rec(polygon, i, j):
    if j < i + 2:
        return 0
    cost = 999999
    for k in range(i + 1, j):
        cost = min(cost, (minCost_rec(polygon, i, k) + minCost_rec(polygon, k, j) +
                          triangle_cost(polygon[i], polygon[k], polygon[j])))
    return cost


def minCost_dynamic(polygon):
    n = len(polygon)
    D = [[0 for _ in range(n)] for _ in range(n)]
    cost = 999999
    for x in range(2, n):
        for i in range(n - x):
            j = i + x
            D[i][j] = cost
            for k in range(i + 1, j):
                new_cost = D[i][k] + D[k][j] + triangle_cost(polygon[i], polygon[k], polygon[j])
                if new_cost < D[i][j]:
                    D[i][j] = new_cost

    return D[0][-1]


def main():
    list_1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    list_2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]
    tab_1 = []
    tab_2 = []
    for i in list_1:
        tab_1.append(Point(i[0], i[1]))
    for i in list_2:
        tab_2.append(Point(i[0], i[1]))

    t_start = time.perf_counter()
    cost_rec_1 = minCost_rec(tab_1, 0, len(tab_1) - 1)
    t_stop = time.perf_counter()
    time_rec_1 = t_stop - t_start

    t_start = time.perf_counter()
    cost_rec_2 = minCost_rec(tab_2, 0, len(tab_2) - 1)
    t_stop = time.perf_counter()
    time_rec_2 = t_stop - t_start

    t_start = time.perf_counter()
    cost_dynamic_1 = minCost_dynamic(tab_1)
    t_stop = time.perf_counter()
    time_dynamic_1 = t_stop - t_start

    t_start = time.perf_counter()
    cost_dynamic_2 = minCost_dynamic(tab_2)
    t_stop = time.perf_counter()
    time_dynamic_2 = t_stop - t_start

    print('rekurencja')
    print(f'{cost_rec_1:.4f}', time_rec_1)
    print(f'{cost_rec_2:.4f}', time_rec_2)

    print('dynamiczne')
    print(f'{cost_dynamic_1:.4f}', time_dynamic_1)
    print(f'{cost_dynamic_2:.4f}', time_dynamic_2)


main()
