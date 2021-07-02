###Source class
import datetime


class Human:

    human_created = 0

    def __init__(self, name, sex, birth):
        self.name = name
        self.sex = sex
        self.birth = int(birth)
        self.list_of_humans = []

        if Human:
            self.human_created += 1
    
    def create_human(self):
        list_of_human = self.list_of_humans
        list_of_human.extend([self.name, self.sex, self.birth])
        print(list_of_human)
    
    def get_humans_age(self):
        today = int(datetime.datetime.now().strftime("%G"))
        age = today - int(self.birth)
        print(f"{self.name}'s age is {age} years old")


h1 = Human(name="first", sex="Male", birth=1)
h1.create_human()
h1.get_humans_age()
print(f"Numbers of human being created: {h1.human_created}")
