from model.toolsbox import ToolsBox
from model.hammers import Hammer
from model.screwsdriver import ScreewDriver

def main():

    ham = Hammer("Hammer", "Black")
    print(ham.add_tools())

    ham3 = Hammer("Hammer", "Red")
    print(ham3.add_tools())


    ham2 = Hammer("Hammer", "Orange")
    print(ham2.add_tools())

    screw = ScreewDriver("Elvis", "blue")
    print(screw.add_tools())

    screw2 = ScreewDriver("Elvis2", "Green")
    print(screw2.add_tools())


    total = Hammer.number_of_tools
    print(f" All Hammers created: {total}")

    totalscrew = ScreewDriver.number_of_tools
    print(f" All Screwdrivers created: {totalscrew}")

if __name__ == "__main__":
    main()




