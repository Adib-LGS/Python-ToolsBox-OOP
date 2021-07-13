from cars import Cars
def main():

    car1 = Cars('Ford', 'Mustang', 'V8', False)
    car1.get_car_make_and_model()
    car1.get_car_engine()
    print(car1)

    """cars2 = Cars(make=str(input("Give us the make: ")), model=str(input("Give us the model: ")), engine=str(input("Give us the engine: ")))
    cars2.get_car_make_and_model()
    cars2.get_car_engine
    print(cars2)"""


if __name__ == "__main__":
    main()