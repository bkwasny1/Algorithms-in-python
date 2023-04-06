#nieskonczone

class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class deleted:
    def __init__(self, key=None, data='deleted'):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        tab = [None for i in range(size)]
        self.tab = tab

    def hash(self, key):
        if isinstance(key, str):
            suma = 0
            for sign in key:
                suma += ord(sign)
            return suma % self.size
        return key % self.size

    def quadratic(self, idx, key, i=0):
        idx_new = idx
        while self.tab[idx_new] is not None and self.tab[idx_new].key != key:
            if self.tab[idx_new].data == 'deleted' and self.tab[idx_new].key is None:
                return (deleted(), idx_new, i)
            idx_new = (idx + self.c1 * i + self.c2 * i**2) % self.size
            i += 1
            if i == self.size + 1:
                return None
        return idx_new

    def search(self, key):
        idx = self.hash(key)
        idx = self.quadratic(idx, key)
        idx_next = idx
        while isinstance(idx_next, tuple):
            idx_next = self.hash(key) + idx_next[2] + 1
            idx_next = self.quadratic(idx_next, key)
        if idx_next is None:
            return None
        elif self.tab[idx_next] is None:
            return None
        else:
            return self.tab[idx_next].data

    def insert(self, key, value):
        idx = self.hash(key)
        idx = self.quadratic(idx, key)
        if idx is None:
            return print('Brak miejsca')
        elif isinstance(idx, tuple):
            self.tab[idx[1]].key, self.tab[idx[1]].data = key, value
        elif self.tab[idx] is None:
            self.tab[idx] = Element(key, value)
        else:
            self.tab[idx].data = value

    def remove(self, key):
        idx = self.hash(key)
        idx = self.quadratic(idx, key)
        if isinstance(idx, tuple):
            return print('Brak danej')
        if self.tab[idx] is not None:
            self.tab[idx] = deleted()
        else:
            return print('Brak danej')

    def __str__(self):
        string = '{'
        for i in range(self.size):
            if self.tab[i] is not None:
                string += f'{self.tab[i].key}:{self.tab[i].data}, '
            else:
                string += 'None, '
        string = string[:-2]
        string += '}'
        return string


def function_1(size, c1, c2):
    tab = HashTable(size, c1, c2)
    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(15):
        tab.insert(keys[i], values[i])
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5, 'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    tab.insert('test', 'W')
    print(tab,'\n')


def function_2(size, c1, c2):
    tab = HashTable(size, c1, c2)
    keys = []
    for i in range(1, 16):
        keys.append(i*13)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(len(keys)):
        tab.insert(keys[i], values[i])
    print(tab, '\n')


function_1(13, 1, 0)

function_2(13, 1, 0)

function_2(13, 0, 1)

