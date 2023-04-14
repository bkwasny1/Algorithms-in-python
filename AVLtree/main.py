class tree_node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.height = 1


class root_node_avl:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.__search(key, self.root)

    def __search(self, key, node):
        if node is None:
            return f'Brak danej o kluczu {key}'
        if key < node.key:
            return self.__search(key, node.left)
        elif key > node.key:
            return self.__search(key, node.right)
        else:
            return node.value

    def insert(self, key, value):
        self.root = self.__insert(key, value, self.root)

    def __insert(self, key, value, node):
        if node is None:
            return tree_node(key, value)
        if key < node.key:
            node.left = self.__insert(key, value, node.left)
        else:
            node.right = self.__insert(key, value, node.right)

        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))

        difference = self.balance_check(node)

        if difference > 1 and key < node.left.key:
            return self.right_rotation(node)

        if difference > 1 and key > node.left.key:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)

        if difference < -1 and key > node.right.key:
            return self.left_rotation(node)

        if difference < -1 and key < node.right.key:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node

    def delete(self, key):
        self.__delete(key, self.root)

    def __delete(self, key, node):
        if node is None:
            return None
        if key < node.key:
            node.left = self.__delete(key, node.left)

        elif key > node.key:
            node.right = self.__delete(key, node.right)

        else:
            if node is None:
                return None
            if node.key > key:
                node.left = self.__delete(key, node.left)
            elif node.key < key:
                node.right = self.__delete(key, node.right)
            if node.left is None and node.right is None:
                return None
            elif node.left is None and node.right is not None:
                return node.right
            elif node.right is None and node.left is not None:
                return node.left
            else:
                parents = node
                successor = node.right
                while successor.left is not None:
                    parents = successor
                    successor = successor.left
                if parents != node:
                    parents.left = successor.right
                else:
                    parents.right = successor.right
                node.key = successor.key

        if node is None:
            return node
        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))
        difference = self.balance_check(node)

        if difference > 1:
            if self.balance_check(node.left) >= 0:
                return self.right_rotation(node)
            else:
                node.left = self.left_rotation(node.left)
                return self.right_rotation(node)
        if difference < -1:
            if self.balance_check(node.right) <= 0:
                return self.left_rotation(node)
            else:
                node.right = self.right_rotation(node.right)
                return self.left_rotation(node)
        return node

    def balance_check(self, node):
        if node is None:
            return 0
        return self.getheight(node.left) - self.getheight(node.right)

    def getheight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)

    def tree_list(self, node):
        if node is None:
            return
        else:
            self.tree_list(node.left)
            print(node.key, node.value, end=',')
            self.tree_list(node.right)

    def left_rotation(self, a):
        b = a.right
        d = b.left
        b.left = a
        a.right = d

        a.height = 1 + max(self.getheight(a.left), self.getheight(a.right))
        b.height = 1 + max(self.getheight(b.left), self.getheight(b.right))
        return b

    def right_rotation(self, c):
        b = c.left
        d = b.right
        b.right = c
        c.left = d

        c.height = 1 + max(self.getheight(c.left), self.getheight(c.right))
        b.height = 1 + max(self.getheight(b.left), self.getheight(b.right))
        return b


def main():
    AVL = root_node_avl()
    keys = [50, 15, 62, 5, 2, 1, 11, 100, 7, 6, 55, 52, 51, 57, 8, 9, 10, 99, 12]
    value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T']
    for i in range(len(keys)):
        AVL.insert(keys[i], value[i])
    AVL.print_tree()
    AVL.tree_list(AVL.root)
    print('\n', AVL.search(10))
    AVL.delete(50)
    AVL.delete(52)
    AVL.delete(11)
    AVL.delete(57)
    AVL.delete(1)
    AVL.delete(12)
    AVL.insert(3, 'AA')
    AVL.insert(4, 'BB')
    AVL.delete(7)
    AVL.delete(8)
    AVL.print_tree()
    AVL.tree_list(AVL.root)


main()

