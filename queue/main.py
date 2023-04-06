#nieskonczone

def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:
    def __init__(self):
        tab = []
        self.tab = realloc(tab, 5)
        self.size = len(self.tab)
        self.record_idx = 0
        self.write_idx = 0

    def is_empty(self):
        if self.record_idx == self.write_idx:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty() is True:
            return None
        else:
            return self.tab[self.record_idx]

    def dequeue(self):
        if self.is_empty() is True:
            return None
        a = self.tab[self.record_idx]
        self.tab[self.record_idx] = None
        self.record_idx += 1
        if self.record_idx == self.size:
            self.record_idx = 0
        return a

    def enqueue(self, data):
        self.tab[self.write_idx] = data
        self.write_idx += 1
        if self.write_idx == self.size:
            self.write_idx = 0
        if self.write_idx == self.record_idx:
            a = self.tab
            self.tab = realloc(self.tab, 2 * self.size)
            for i in range(1, self.size):
                self.tab[i+self.size - 1], self.tab[i] = a[i], None
            self.tab[0], self.tab[-1] = None, self.tab[0]
            self.write_idx = 0
            self.record_idx = self.size
            self.size *= 2

    def __str__(self):
        if self.is_empty() is True:
            return '[None]'
        else:
            string = '['
            n = self.record_idx
            for i in range(self.size):
                string += f'{self.tab[n]}, '
                n += 1
                if n == self.size:
                    n = 0
                if n == self.write_idx:
                    break
            string = string[:-2]
            string += ']'
            return string

    def write_table(self):
        string = '['
        for i in range(self.size):
            string += f'{self.tab[i]}, '
        string = string[:-2]
        string += ']'
        return string


que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que.dequeue())
print(que.peek())
print(que)
que.enqueue(5)
que.enqueue(6)
que.enqueue(7)
que.enqueue(8)
print(que.write_table())
for i in range(7):
    print(que.dequeue())
print(que.is_empty())
