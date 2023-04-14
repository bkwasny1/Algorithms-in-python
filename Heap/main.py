#skonczone

class Element:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __str__(self):
        return f"{self.__priority} : {self.__data}"


class Heap:
    def __init__(self):
        self.tab = []
        self.heap_size = 0

    def is_empty(self):
        if self.heap_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.heap_size == 0:
            return None
        return self.tab[0]

    def dequeue(self):
        if self.heap_size == 0:
            return None
        old_root = self.tab[0]
        self.tab[0], self.tab[self.heap_size - 1] = self.tab[self.heap_size - 1], self.tab[0]
        self.heap_size -= 1
        idx = 0
        left_idx = self.left(idx)
        right_idx = self.right(idx)

        while self.tab[left_idx] > self.tab[idx] or self.tab[right_idx] > self.tab[idx]:
            if self.heap_size == 2 and self.tab[left_idx] > self.tab[idx]:
                self.tab[0], self.tab[1] = self.tab[1], self.tab[0]
            elif self.heap_size == 2:
                break
            elif self.heap_size == 1:
                break
            elif self.tab[left_idx] > self.tab[idx] and self.tab[right_idx] > self.tab[idx]:
                if self.tab[left_idx] > self.tab[right_idx]:
                    self.tab[left_idx], self.tab[idx] = self.tab[idx], self.tab[left_idx]
                    idx = self.left(idx)
                    left_idx = self.left(idx)
                    right_idx = self.right(idx)
                else:
                    self.tab[right_idx], self.tab[idx] = self.tab[idx], self.tab[right_idx]
                    idx = self.right(idx)
                    left_idx = self.left(idx)
                    right_idx = self.right(idx)
            elif self.tab[left_idx] > self.tab[idx]:
                self.tab[left_idx], self.tab[idx] = self.tab[idx], self.tab[left_idx]
                idx = self.left(idx)
                left_idx = self.left(idx)
                right_idx = self.right(idx)
            else:
                self.tab[right_idx], self.tab[idx] = self.tab[idx], self.tab[right_idx]
                idx = self.right(idx)
                left_idx = self.left(idx)
                right_idx = self.right(idx)
            if left_idx >= self.heap_size or right_idx >= self.heap_size or idx >= self.heap_size:
                break

        return old_root

    def enqueue(self, element):
        if self.heap_size == len(self.tab):
            self.tab.append(element)
            self.heap_size += 1
        else:
            self.tab[self.heap_size] = element
            self.heap_size += 1
        idx = self.heap_size - 1
        parent_idx = self.parent(idx)
        while self.tab[parent_idx] < self.tab[idx]:
            self.tab[parent_idx], self.tab[idx] = self.tab[idx], self.tab[parent_idx]
            idx = parent_idx
            parent_idx = self.parent(idx)

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def parent(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx >= 0:
            return parent_idx
        else:
            return 0

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def main():
    heap = Heap()
    priority = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    data = 'GRYMOTYLA'
    for i in range(0, len(priority)):
        heap.enqueue(Element(data[i], priority[i]))
    heap.print_tree(0, 0)
    heap.print_tab()
    deq1 = heap.dequeue()
    print(heap.peek())
    heap.print_tab()
    print(deq1)
    while heap.is_empty() is False:
        print(heap.dequeue())
    heap.print_tab()


main()
