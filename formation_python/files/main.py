#########CREATE FILE - OPEN IT############
import pickle

class Player:

    def __init__(self, name, level) -> None:
        self.name = name
        self.level = level

    def get_player_data(self):
        print("Name: " , self.name  , "Level" , self.level)


    @classmethod
    def create_file(cls):
        with open("player.data", "wb") as player_file:
            record = pickle.Pickler(player_file)
            record.dump(p1)
    
    
    @classmethod
    def open_file(cls):
        with open("player.data", "rb") as player_file:
            get_record = pickle.Unpickler(player_file)
            get_record.load()
            
            

p1 = Player("Leonidas", 49)
p1.create_file()
p1.open_file()
p1.get_player_data()

"""with  open("../files/data.txt", "r") as files:
            content = files.read()
            print(content)"""