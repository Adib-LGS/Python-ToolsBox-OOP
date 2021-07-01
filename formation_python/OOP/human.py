###Source class

class Human:

    def __init__(self, name, sex, birth):
        self.name = name
        self.sex = sex
        self.birth = birth

        self.list_of_humans = []
    
    def create_human(self):
        self.list_of_humans.extend([self.name, self.sex, self.birth])
        list_of_human = self.list_of_humans
        print(list_of_human)
    


h1 = Human("first", "Male", "1-1-0001")
h1.create_human()
print(h1)