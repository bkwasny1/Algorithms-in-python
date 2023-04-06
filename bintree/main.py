class tree_node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class root_node:
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
            return node
        elif key > node.key:
            node.right = self.__insert(key, value, node.right)
            return node
        else:
            node.value = value
            return node

    def delete(self, key):
        self.__delete(key, self.root)

    def __delete(self, key, node):
        if node is None:
            return None
        if node.key > key:
            node.left = self.__delete(key, node.left)
            return node
        elif node.key < key:
            node.right = self.__delete(key, node.right)
            return node
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
            return node

    def height(self, node):
        if node is None:
            return 0
        else:
            left_ = self.height(node.left)
            right_ = self.height(node.right)
            return 1 + max(left_, right_)

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
        if node is not None:
            self.tree_list(node.left)
            print(node.key, node.value, end=',')
            self.tree_list(node.right)


def main():
    BST = root_node()
    keys = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]
    value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    for i in range(len(keys)):
        BST.insert(keys[i], value[i])
    BST.print_tree()
    BST.tree_list(BST.root)
    print()
    print(BST.search(24))
    BST.insert(20, 'AA')
    BST.insert(6, 'M')
    BST.delete(62)
    BST.insert(59, 'N')
    BST.insert(100, 'P')
    BST.delete(8)
    BST.delete(15)
    BST.insert(55, 'R')
    BST.delete(50)
    BST.delete(5)
    BST.delete(24)
    print(BST.height(BST.root))
    BST.tree_list(BST.root)
    print()
    BST.print_tree()


main()
