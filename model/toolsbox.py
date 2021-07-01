"""Abstract class Using by others to stock and get Tools Properties"""

from builtins import isinstance
from abc import ABC, abstractmethod

class ToolsBox(ABC):

    MAX_NUMBER_OF_TOOLS = 5
    number_of_tools = 0

    def __init__(self, name, color):

        self.toolbox = []
        self.name = name
        self.color = color
        
        if ToolsBox:
            self.number_of_tools += 1
            
        if isinstance(self, __class__):
            self.MAX_NUMBER_OF_TOOLS -= self.number_of_tools
            if self.MAX_NUMBER_OF_TOOLS == 0:
                print("No place anymore")


    def get_tool_name(self):
        return self.name


    def add_tools(self):
        if self.number_of_tools < self.MAX_NUMBER_OF_TOOLS:
            self.toolbox.extend([self])
            self.MAX_NUMBER_OF_TOOLS -= self.number_of_tools
            return f"There's actually: {self.number_of_tools}-{self.name} in the ToolBox"

        elif self.MAX_NUMBER_OF_TOOLS == 0:
            print(f"Sorry the tool box is full {self.MAX_NUMBER_OF_TOOLS}")
    

    def remove_tools(self):
        pass    
    

    def paint(self, color):
        self.color = color



        
