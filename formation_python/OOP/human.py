###Source class###
import datetime


class Human:

    # class attributes increase with new created human
    human_created = 0

    humans_planet = "Hearth"

    def __init__(self, name, sex, birth):
        self.name = name
        self._sex = sex
        self._birth = int(birth)
        self.list_of_humans = []

        if Human:
            self.human_created += 1

    #Encapsulate properties to protect parametters
    def _getsex(self):
        try:
            if self._sex == "Male" or self._sex == "Female":
                return self._sex
            elif self._sex == "":
                print("Human must biologically be ('Male') or ('Female')")
            elif self._sex != "":
                print("Human must biologically be ('Male') or ('Female')")
        except ValueError:
            print("Only string are allowed / integers or floats are not accepted")
    
    def _getbirth(self):
        try:
            if self._birth >= 1:
                return self._birth
            else:
                print('the first human was born in the year 1')
        except ValueError:
            print("Only integer are allowed / float or strings are not accepted")

    birth = property(_getbirth)
    sex = property(_getsex)

    
    def create_human(self):
        list_of_human = self.list_of_humans
        list_of_human.extend([self.name, self.sex, self.birth])
        print(list_of_human)
    

    def get_humans_age(self):
        if self._birth >= 1:
            today = int(datetime.datetime.now().strftime("%G"))
            age = today - int(self._birth)
            print(f"{self.name}'s age is {age} years old")
        else:
            print("You cannot calculate the age cause age must be > 1")


    @classmethod
    def change_humans_planet(cls, new_planet_name = "Heart"):
        Human.humans_planet = new_planet_name
        return new_planet_name


    @staticmethod
    def whats_an_human() -> str:
        print('Humans cannot be defined...')


h1 = Human(name="First", sex="Male", birth=1)
h1.create_human()
h1.get_humans_age()
print(f"Numbers of human being created: {h1.human_created}")
print(f"{h1.name} was laid on {Human.change_humans_planet('Mars')}")
Human.whats_an_human()

h2 = Human("Second", "Female", 1)
h2.create_human()
h2.get_humans_age()