class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self):
        return f"{self.name}.{self.extension} ({self.size} bytes)"
