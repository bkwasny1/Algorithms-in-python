class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class deleted:
    def __init__(self, key, data=None):
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

    def quadratic(self, idx, key, i=1):
        a = 0
        while self.tab[idx] is not None and self.tab[idx].key != key:
            idx = (idx + self.c1 * i + self.c2 * i**2) % self.size
            a += 1
            if a == self.size + 1:
                return None
        return idx

    def search(self, key):
        idx = self.hash(key)
        idx = self.quadratic(idx, key)
        if idx is None:
            return None
        elif self.tab[idx] is None or isinstance(self.tab[idx], deleted):
            return None
        else:
            return self.tab[idx].data

    def insert(self, key, value):
        idx = self.hash(key)
        if self.tab[idx] is None or isinstance(self.tab[idx], deleted):
            self.tab[idx] = Element(key, value)
        else:
            i = 1
            while True:
                new_idx = (idx + self.c1 * i + self.c2 * i**2) % self.size
                if self.tab[new_idx] is None or isinstance(self.tab[new_idx], deleted):
                    self.tab[new_idx] = Element(key, value)
                    break
                if i > 100:
                    break
                i += 1

    def remove(self, key):
        idx = self.hash(key)
        idx = self.quadratic(idx, key)
        if self.tab[idx] is not None:
            self.tab[idx] = deleted(key)
        else:
            print(f'brak danej o kluczu {key}')

    def __str__(self):
        string = '{'
        for i in range(self.size):
            if self.tab[i] is not None and not isinstance(self.tab[i], deleted):
                string += f'{self.tab[i].key}:{self.tab[i].data}, '
            else:
                string += 'None, '
        string = string[:-2]
        string += '}'
        return string


def function_1(size, c1=1, c2=0):
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
    tab.insert('W', 'test')
    print(tab)


function_1(13)


def function_2(size, c1=1, c2=0):
    tab = HashTable(size, c1, c2)
    keys = []
    for i in range(1, 16):
        keys.append(i*13)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(len(keys)):
        tab.insert(keys[i], values[i])
    print(tab)


#print('funkcja2_1')
#function_2(13, 1, 0)

#print('funkcja2_2')
#function_2(13, 0, 1)
