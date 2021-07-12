#Show the ingredient of the menu chosen by the customer

menu = {"Tapas" : ["Tomatoes, Olive, Chicken"],
    "Fajitas" : ["Tortilla, Chicken, Onion, Pepper"]}

food = str(input("Choose between [Tapas] or [Fajitas]: "))
capital_food = food.capitalize()

if capital_food in menu:
    print(f"Meal name -> {capital_food} and the ingredients -> {menu[capital_food]}")
else:
    print('SOrry error')
