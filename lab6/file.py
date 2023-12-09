"""this is description of File"""
class File:
    """class File"""

    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

        self.validate_size(size)

    @staticmethod
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


class MyException(Exception):
    """Exception that is raised when there's unexpected"""
    def init(self, message="Це моя власна помилка!"):
        """this is MyException description"""
        super().__init__(message)
