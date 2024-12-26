"""`Memento_` is a behavioral design pattern that allows saving and
restoring the state of an object without revealing its internal structure.
Memento creates a snapshot of the object's state, which can be used to restore it later.

.. _Momento:
    https://refactoring.guru/design-patterns/memento

"""


# The object that we want to save and restore its state.
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_state()


# Memento that stores the state of the TextEditor.
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


# Storage for mementos.
class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento):
        self._mementos.append(memento)

    def pop(self):
        if self._mementos:
            return self._mementos.pop()
        return None


# The client's code.
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello, ")
    history.push(editor.save())

    editor.write("world!")
    print("Current state: ", editor.get_content())

    editor.restore(history.pop())
    print("After restoring: ", editor.get_content())
