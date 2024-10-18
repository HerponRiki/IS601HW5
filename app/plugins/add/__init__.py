from app.commands import Command
from calculator import operations

class AdditionCommand(Command):
    def execute(self):
        return operations.add
    