#nieskonczone
from random import random


class Element:
    def __init__(self, key, value, levels):
        self.key = key
        self.value = value
        self.levels = levels
        self.tab_next = [None for i in range(levels)]


class SkipList:
    def __init__(self, maxLevel):
        self.maxLevel = maxLevel
        self.head = Element(None, None, maxLevel)

    def randomLevel(self, p=0.5):
        lvl = 1
        while random() < p and lvl < self.maxLevel:
            lvl = lvl + 1
        return lvl

    def search(self, key):
        current = self.head
        for i in range(self.maxLevel - 1, -1, -1):
            while current.tab_next[i] and current.tab_next[i].key < key:
                current = current.tab_next[i]
        current = current.tab_next[0]

        if current and current.key == key:
            return current.value
        else:
            return None

    def insert(self, key, value):
        lvl = self.randomLevel()
        new_node = Element(key, value, lvl)
        current = self.head
        prev = [None for i in range(self.maxLevel)]
        for i in range(lvl - 1, -1, -1):
            while current.tab_next[i] and current.tab_next[i].key < key:
                current = current.tab_next[i]
            prev[i] = current
        current = current.tab_next[0]

        if current is None or current.key != key:
            for i in range(lvl):
                new_node.tab_next[i] = prev[i].tab_next[i]
                prev[i].tab_next[i] = new_node
        if current and current.key == key:
            current.value = value

    def remove(self, key):
        current = self.head
        prev = [None for i in range(self.maxLevel)]
        for i in range(self.maxLevel - 1, -1, -1):
            while current.tab_next[i] and current.tab_next[i].key < key:
                current = current.tab_next[i]
            prev[i] = current
        current = current.tab_next[0]

        if current and current.key == key:
            for i in range(current.levels):
                prev[i].tab_next[i] = current.tab_next[i]
        else:
            return None

    def __str__(self):
        current = self.head
        current = current.tab_next[0]
        string = '{'
        while current.tab_next[0] is not None:
            string += f'{current.key}:{current.value}, '
            current = current.tab_next[0]
        string += f'{current.key}:{current.value}, '
        string = string[:-2]
        string += '}'
        return string

    def displayList_(self):
        node = self.head.tab_next[0]
        keys = []
        while (node != None):
            keys.append(node.key)
            node = node.tab_next[0]

        for lvl in range(self.maxLevel - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.tab_next[lvl]
            idx = 0
            while (node != None):
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.tab_next[lvl]
            print("")


def main():
    test = SkipList(4)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        test.insert(i, values[i - 1])
    test.displayList_()
    print(test.search(2))
    test.insert(2, 'Z')
    print(test.search(2))
    test.remove(5)
    test.remove(6)
    test.remove(7)
    print(test)
    test.insert(6, 'W')
    print(test, '\n')

    test2 = SkipList(4)
    for i in range(15, 0, -1):
        test2.insert(i, values[i - 1])
    test2.displayList_()
    print(test2.search(2))
    test2.insert(2, 'Z')
    print(test2.search(2))
    test2.remove(5)
    test2.remove(6)
    test2.remove(7)
    print(test2)
    test2.insert(6, 'W')
    print(test2, '\n')


main()

