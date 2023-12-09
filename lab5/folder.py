from file import File


class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def __str__(self):
        return self.name


    def print_tree(self, node=None, indent=""):
        if node==None:
            node = self
        print(indent + str(node))
        if isinstance(node, Folder):
            for item in node.contents:
                self.print_tree(item, indent + "  ")


    def find_longest_path(self, node=None, current_path=""):
        if node==None:
            node = self
        if isinstance(node, File):
            return current_path + node.name + '.' + node.extension
        longest_path = ""
        for item in node.contents:
            path = self.find_longest_path(item, current_path + node.name + '/')
            if len(path) > len(longest_path):
                longest_path = path
        return longest_path
