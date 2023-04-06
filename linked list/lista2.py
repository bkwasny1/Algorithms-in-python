class Element:
    def __init__(self, data=None, next_elem=None, prev_elem=None):
        self.data = data
        self.next = next_elem
        self.prev = prev_elem


class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_element = Element(data, self.head)
        if self.head is not None:
            self.head.prev = new_element
        self.head = new_element
        if self.tail is None:
            self.tail = new_element

    def append(self, elem):
        new_elem = Element(elem, None, self.tail)
        if self.tail is not None:
            self.tail.next = new_elem
        self.tail = new_elem
        if self.head is None:
            self.head = new_elem

    def remove(self):
        if self.head is None:
            return None
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

    def remove_end(self):
        if self.tail is None:
            return None
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        leng = 0
        a = self.head
        while a is not None:
            leng += 1
            a = a.next
        return leng

    def get(self):
        if self.head is not None:
            return self.head.data
        else:
            return None

    def to_string(self):
        string = ''
        a = self.head
        while a is not None:
            string += f'-> {a.data}\n'
            a = a.next
        print(string)


python_list = [('AGH', 'Kraków', 1919),
               ('UJ', 'Kraków', 1364),
               ('PW', 'Warszawa', 1915),
               ('UW', 'Warszawa', 1915),
               ('UP', 'Poznań', 1919),
               ('PG', 'Gdańsk', 1945)]


uczelnie = Lista()
uczelnie.append(python_list[0])
uczelnie.append(python_list[1])
uczelnie.append(python_list[2])
uczelnie.add(python_list[3])
uczelnie.add(python_list[4])
uczelnie.add(python_list[5])
uczelnie.to_string()
print(uczelnie.length(), '\n')
uczelnie.remove()
print(uczelnie.get(), '\n')
uczelnie.remove_end()
uczelnie.to_string()
uczelnie.destroy()
print(uczelnie.is_empty())
uczelnie.remove()
uczelnie.remove_end()
