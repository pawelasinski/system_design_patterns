"""`Composite`_ — is a structural design pattern that allows you to group
objects into a tree structure in order to work with them uniformly, i.e. allows clients
to process individual objects and their groups (composite objects) in the same way.

.. _Composite:
   https://refactoring.guru/ru/design-patterns/composite

"""
from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


# Individual object (file).
class File(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        return f"File: {self.name}"


# Composite object (directory).
class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = [f"Directory: {self.name}"]
        for child in self.children:
            results.append(f"  {child.operation()}")
        return "\n".join(results)


if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    folder1 = Directory("folder1")
    folder2 = Directory("folder2")

    # Build the tree structure.
    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)
    root = Directory("root")
    root.add(folder1)
    root.add(folder2)

    print(root.operation())
