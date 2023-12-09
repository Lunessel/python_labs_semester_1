"""this is description of classes"""
import logging


class MyException(Exception):
    """Exception that is raised when there's unexpected"""
    def init(self, message="Це моя власна помилка!"):
        """this is MyException description"""
        super().__init__(message)


def logged(exception: Exception, mode: str = "console"):
    """it's my logger for Exeptions"""
    def wrapper(func):

        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.DEBUG, encoding="utf-8")
                    logging.error(e)
                else:
                    print(f"Error: {e}")
            finally:
                if mode == "file":
                    logging.shutdown()
        return inner
    return wrapper


class File:
    """class File"""

    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

        self.validate_size(size)

    @staticmethod
    @logged(MyException, "console")
    def validate_size(size):
        """validating size field"""
        if not isinstance(size, int):
            raise MyException("Розмір має бути числом")

    def __str__(self):
        """stringing"""
        return f"{self.name}.{self.extension} ({self.size} bytes)"

    def __repr__(self):
        """stringing"""
        return f"{self.name}.{self.extension} ({self.size} bytes)"


class Folder:
    """class Folder"""
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, item):
        """this is add method"""
        self.contents.append(item)

    def __str__(self):
        return self.name

    def print_tree(self, node=None, indent=""):
        """this is print_tree method"""
        if node is None:
            node = self
        print(indent + str(node))
        if isinstance(node, Folder):
            for item in node.contents:
                self.print_tree(item, indent + "  ")

    def find_longest_path(self, node=None, current_path=""):
        """this is find-longest-path method"""
        if node is None:
            node = self
        if isinstance(node, File):
            return current_path + node.name + '.' + node.extension
        longest_path = ""
        for item in node.contents:
            path = self.find_longest_path(item, current_path + node.name + '/')
            if len(path) > len(longest_path):
                longest_path = path
        return longest_path
