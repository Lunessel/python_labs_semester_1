"""import Classes and pytest"""
import sys
from io import StringIO
import pytest
from file import File, MyException
from folder import Folder


@pytest.fixture(name="root")
def sample_root():
    """defining folders and files and making bond with them"""
    folder = Folder("root")
    file1 = File("file1", "txt", 1024)
    file2 = File("file2", "txt", 2048)
    folder.add(file1)
    folder.add(file2)
    return folder


def test_add_positive():
    """positive testing of function add"""
    folder = Folder("Programs")
    file = File("VS Code", "exe", 2000)
    folder.add(file)
    assert folder.contents[0] is file


def test_add_negative():
    """negative testing of function add"""
    folder = Folder("Programs")
    vscode = File("VS Code", "exe", 2000)
    folder.add(vscode)
    folder.add(vscode)
    assert len(folder.contents) == 1


def test_folder_print_tree(root):
    """test method print_tree"""
    table = File("table", "sql", 2423)
    db = Folder("db")
    db.add(table)
    root.add(db)
    output_buffer = StringIO()
    sys.stdout = output_buffer
    root.print_tree()
    sys.stdout = sys.__stdout__
    output_value = output_buffer.getvalue()
    assert output_value == "root\n  file1.txt (1024 bytes)\n  file2.txt (2048 bytes)\n  db\n    table.sql (2423 bytes)\n"


def test_folder_find_longest_path():
    """test methoudfind_longest_path"""
    root = Folder("Root")
    folder1 = Folder("Folder1")
    folder2 = Folder("Folder2")
    folder3 = Folder("Folder3")
    file1 = File("Document", "txt", 100)
    file2 = File("Image", "jpg", 200)
    file3 = File("Spreadsheet", "xlsx", 150)
    file4 = File("Video", "mp4", 500)
    file5 = File("Audio", "mp3", 300)


    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)
    folder2.add(file4)
    folder2.add(folder3)
    folder3.add(file5)
    root.add(folder1)
    root.add(folder2)
    assert root.find_longest_path() == "Root/Folder2/Folder3/Audio.mp3"


def test_size_type():
    """test type of size field"""
    with pytest.raises(MyException):
        File("cat", "img", "23a")
