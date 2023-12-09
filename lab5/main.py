from file import File
from folder import Folder


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

print("tree of files:")
root.print_tree()

longest_path = root.find_longest_path()
print(f"longest way to object: {longest_path}")