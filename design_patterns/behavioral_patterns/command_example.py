"""Command

`Command_` is a behavioral design pattern that encapsulates a request as an object,
storing all the necessary details to execute, delay, queue, or undo the request when needed.
This abstraction allows greater flexibility in handling operations dynamically.

Why use it?
* Decouples sender and receiver (the request issuer doesn’t need to know how it will be executed).
* Supports undo/redo operations (essential for actions that need reversibility
    (e.g., text editors, transactions)).
* Facilitates request queuing and scheduling (enables delayed or batched execution).
* Improves extensibility (new commands can be added without modifying existing code).

.. _Command:
    https://refactoring.guru/design-patterns/command

"""


# Command's interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


# Particular command's implementations
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


# Receiver
class Light:
    def on(self):
        print("The light is switched on!")

    def off(self):
        print("The light is switched off!")


# Invoker
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


if __name__ == "__main__":
    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()

    remote.execute_command(light_on)
    remote.execute_command(light_off)

    print("\nCancelling the latest command: ")
    remote.undo_last_command()
