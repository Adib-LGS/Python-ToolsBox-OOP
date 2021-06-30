"""Create Hammer"""

from model.toolsbox import ToolsBox

class Hammer(ToolsBox):

    number_of_tools = 0

    def __init__(self, name, color):
        super().__init__(name, color)
        self.toolbox = []

        Hammer.number_of_tools += 1

    def hammer_in(self, nail):
        nail.nail_in()

    def remove(self, nail):
        nail.remove()