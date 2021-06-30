"""Create Nail"""

from model.toolsbox import ToolsBox

class Nail(ToolsBox):
    
    def __init__(self, name):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False
    
    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
        self.in_wall = True
    
    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
        self.in_wall = False