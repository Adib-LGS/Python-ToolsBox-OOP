"""Create Screw Driver"""

from model.toolsbox import ToolsBox

class ScreewDriver(ToolsBox):

    number_of_tools = 0

    def __init__(self,name, color, size = None):
        super().__init__(name, color)
        
        self.toolbox = []
        self.size = size

        ScreewDriver.number_of_tools += 1
        

    def tighten(self, screw):
        screw.tighten()

    def loosen(self, screw):
        screw.loosen()
