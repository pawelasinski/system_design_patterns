"""`Command_` is a behavioral design pattern that turns a request into a stand-alone object
that contains all information about the request. This transformation lets you pass requests
as a method arguments, delay or queue a request’s execution, and support undoable operations.

.. _Command:
    https://refactoring.guru/design-patterns/command

"""


# The command's interface.
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


# The particular command's implementations.
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# Receiver.
class Light:
    def on(self):
        print("The light is switched on!")

    def off(self):
        print("The light is switched off!")


# Invoker.
class RemoteControl:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()


# The client's code.
if __name__ == "__main__":
    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.execute_command(light_on)
    remote.execute_command(light_off)

    print("\nCancelling the latest command: ")
    remote.undo_last_command()
