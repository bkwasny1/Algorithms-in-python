class Element:
    def __init__(self, data=None, next_elem=None):
        self.data = data
        self.next = next_elem


class Lista:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, data):
        new_element = Element(data, self.head)
        self.head = new_element

    def append(self, elem):
        new_elem = Element(elem)
        if self.head is None:
            self.head = new_elem
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = new_elem

    def remove(self):
        if self.head is None:
            return None
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            return None
        else:
            leng = 0
            a = self.head
            while a.next is not None:
                leng += 1
                a = a.next
            b = self.head
            while leng != 2:
                b = b.next
                leng -= 1
            b.next = None

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
