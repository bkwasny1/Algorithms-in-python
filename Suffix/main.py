class TreeNode:
    def __init__(self):
        self.chars = []
        self.children = []
        self.size = 0
        self.end_of_word = False

    def __repr__(self):
        return str(self.chars)


class SuffixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        current_node = self.root
        for i in word:
            if i not in current_node.chars:
                new_node = TreeNode()
                current_node.children.append(new_node)
                current_node.chars.append(i)
                if i == '/':
                    new_node.chars.append('/0')
                    current_node.size += 1
                    break
                current_node.size += 1
                current_node = new_node
            else:
                index = current_node.chars.index(i)
                current_node = current_node.children[index]
        current_node.end_of_word = True

    def build_suffix_tree(self, text):
        for i in range(len(text)):
            suffix = text[i:]
            self.insert(suffix)

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, level):
        if node is not None:
            for i in range(node.size):
                if node.children[i].end_of_word:
                    print(level * '  ', node.chars[i], '\\0')
                else:
                    if node.chars[i] == '/':
                        continue
                    print(level * '  ', node.chars[i])
                self._print_tree(node.children[i], level + 1)


tree = SuffixTree()
tree.build_suffix_tree("banana/")
tree.print_tree()
