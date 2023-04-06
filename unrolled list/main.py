#skonczone

size = 6


class Tablica:
    def __init__(self):
        self.tab = [None for i in range(size)]
        self.elem_counter = 0
        self.next = None


class Rozwinietalista:
    def __init__(self):
        self.head = None

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
        if self.head is None:
            self.head = Tablica()
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

    def delete(self, index):
        current = self.head

        while current is not None:
            if index <= current.elem_counter:
                if current.elem_counter >= size//2 + 1:
                    old = current.tab[:]
                    current.elem_counter -= 1
                    current.tab[current.elem_counter] = None
                    for i in range(index, current.elem_counter ):
                        current.tab[i] = old[i+1]
                    return

                else:
                    old = current.tab[:]
                    current.elem_counter -= 1
                    current.tab[current.elem_counter] = None
                    for i in range(index, current.elem_counter):
                        current.tab[i] = old[i + 1]
                    if current.next is not None:
                        current.tab[current.elem_counter] = current.next.tab[0]
                        current.next.elem_counter -= 1
                        if current.next.elem_counter < size//2:
                            j = 1
                            for i in range(current.elem_counter, current.elem_counter+current.next.elem_counter):
                                current.tab[i+1] = current.next.tab[j]
                                j += 1
                            current.next = current.next.next
                        else:
                            current.next.elem_counter -= 1
                            old = current.next.tab[:]
                            for i in range(current.next.elem_counter):
                                current.next.tab[i] = old[i+1]
                    return

            index -= current.elem_counter
            current = current.next

    def __str__(self):
        string = '['
        current = self.head
        while current is not None:
            string += f'{current.tab},\n'
            current = current.next
        string = string[:-2]
        string += ']'
        return string


list = Rozwinietalista()
for i in range(10):
    list.insert(i, i + 1)
print(list.get(4))
list.insert(1, 10)
list.insert(8, 11)
print(list)
list.delete(1)
list.delete(2)
print(list)
