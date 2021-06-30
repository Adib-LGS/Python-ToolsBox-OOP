"""Create Screw"""

from model.toolsbox import ToolsBox

class Screw(ToolsBox):
     
    MAX_TIGHTNESS = 5
    
    def __init__(self, name="Screw"):
        """Initialise son degré de serrage."""
        self.tightness = 0
    
    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
        self.tightness -= 1
    
    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
        self.tightness += 1
    