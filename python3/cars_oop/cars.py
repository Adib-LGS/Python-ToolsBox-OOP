from random import choice

class Cars():

    def __init__(self, make, model, engine, is_available=True) -> None:
        self.make = make
        self.model = model
        self.engine = engine
        self.is_available = is_available
        self.random_make = []

    def get_car_make_and_model(self):
        if self.is_available:
            print(f"Make: {self.make} , Model: {self.model}, Engine: {self.engine}")
        else:
            print(f"{self.make} {self.model} is no longer available")

    def get_car_engine(self):
        print(self.engine)

    #Useless for the moment
    def random_cars_make(self, *args):
        random_make = self.random_make
        for i in random_make:
            i.append(args)
        print(choice(args))
        