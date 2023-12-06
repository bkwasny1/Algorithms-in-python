import random

class SkipListNode:
    def __init__(self, key, value, height):
        self.key = key
        self.value = value
        self.next = [None]*height

class SkipList:
    def __init__(self, max_height):
        self.max_height = max_height
        self.head = SkipListNode(None, None, max_height)

    def search(self, key):
        node = self.head
        for i in range(self.max_height-1, -1, -1):
            while node.next[i] and node.next[i].key < key:
                node = node.next[i]
        if node.next[0] and node.next[0].key == key:
            return node.next[0].value
        return None

    def insert(self, key, value):
        prev = [None]*self.max_height
        node = self.head
        for i in range(self.max_height-1, -1, -1):
            while node.next[i] and node.next[i].key < key:
                node = node.next[i]
            prev[i] = node
        node = node.next[0]
        if node and node.key == key:
            node.value = value
        else:
            height = 1
            while random.random() < 0.5 and height < self.max_height:
                height += 1
            new_node = SkipListNode(key, value, height)
            for i in range(height):
                new_node.next[i] = prev[i].next[i]
                prev[i].next[i] = new_node

    def remove(self, key):
        prev = [None]*self.max_height
        node = self.head
        for i in range(self.max_height-1, -1, -1):
            while node.next[i] and node.next[i].key < key:
                node = node.next[i]
            prev[i] = node
        node = node.next[0]
        if node and node.key == key:
            for i in range(len(node.next)):
                if prev[i].next[i] != node:
                    break
                prev[i].next[i] = node.next[i]
            del node

    def __str__(self):
        result = []
        node = self.head.next[0]
        while node:
            result.append((node.key, node.value))
            node = node.next[0]
        return "poziom 0: " + str(result)


