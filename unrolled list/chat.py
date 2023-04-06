size = 6

class Tablica:
    def __init__(self):
        self.tab = [None for i in range(size)]
        self.elem_counter = 0
        self.next = None


class Wiazanalista:
    def __init__(self):
        self.head = Tablica()

    def get(self, index):
        a = self.head
        if a is None:
            return []
        counter = a.elem_counter
        while index >= counter:
            index -= a.elem_counter
            a = a.next
        return a.tab[int(index)]

    def insert(self, index, data):
        current = self.head
        while current is not None:
            if index <= current.elem_counter:
                if current.elem_counter == size:
                    new = Tablica()
                    new.tab[:size // 2] = current.tab[size // 2:]
                    new.elem_counter = size - size // 2
                    current.elem_counter = size // 2
                    for i in range(size // 2, size):
                        current.tab[i] = None
                    if current.next is not None:
                        new.next = current.next
                    current.next = new
                    if index == current.elem_counter:
                        current = new

                else:
                    for i in range(current.elem_counter - 1, index - 1, -1):
                        current.tab[i + 1] = current.tab[i]
                    current.tab[index] = data
                    current.elem_counter += 1
                    return

            index -= current.elem_counter
            current = current.next

        while index > 0:
            new = Tablica()
            index -= size
        new = Tablica()
        new.tab[0] = data
        new.elem_counter = 1

    def delete(self, index):
        pass

    def __str__(self):
        string = '['
        current = self.head
        while current is not None:
            string += f'{current.tab},\n'
            current = current.next
        string = string[:-2]
        string += ']'
        return string


list = Wiazanalista()
list.insert(0, 1)
list.insert(1, 2)
list.insert(2, 3)
list.insert(3, 4)
list.insert(4, 5)
list.insert(5, 6)
list.insert(6, 7)
list.insert(7, 8)
list.insert(8, 9)
list.insert(1, 10)
print(list)
list.insert(8, 11)
list.insert(20, 98)
print(list)


