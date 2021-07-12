#Show the ingredient of the menu chosen by the customer
menu = {"Tapas" : ["Tomatoes, Olive, Chicken"],
    "Fajitas" : ["Tortilla, Chicken, Onion, Pepper"]}

continue_visit = True

print("Welcome to Tex-Mex Python3 \n")

#Asking question untill client decide to order or exit
while continue_visit:
    client_choose = str(input("""Choose [Menu] to see the menu -
    [Food] to order - 
    [Help] for more details and 
    [Exit] if you want to quit: \n"""))

    client_choose_capital = client_choose.capitalize()

    if client_choose_capital == "Menu":
        print(f"THERE IS THE ACTUAL MENU:\n {menu} ")
        continue_visit

    elif client_choose_capital == "Food":
        food = str(input("Choose between [Tapas] or [Fajitas]: "))
        capital_food = food.capitalize()

        if capital_food in menu:
            print(f"Meal name -> {capital_food} and the ingredients -> {menu[capital_food]}")
            continue_visit = False
        else:
            print('SOrry error')
            continue_visit = False
            break
            
    elif client_choose_capital == "Help":
        print("Help MOuahahahahaha what a Joke Mouahahaha")
        continue_visit

    elif client_choose_capital == "Exit":
        print("See you soon - We're sur youll be back HHAHAHAHAHAHHAH")
        continue_visit = False
        break

    else:
        print("Sorry you can't do this operation")
        continue_visit

