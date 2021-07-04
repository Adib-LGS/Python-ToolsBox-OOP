#Create Tuple == Immutable Cintainer create Constant and element axcess
tuple = (1,2,3,34)
print(tuple[-1])

#multiple affectation of values
(number1, number2) = (78, 92)
tuple_number = (number1, number2)
print(tuple_number)

#Return Tupple with 2 values in function
def get_player_position() -> tuple:
    posX = 33
    posY = 26

    return (posX, posY)

coordX = 0
coordY = 0

#before
print(f"Play position: {coordX} {coordY}")

(coordX, coordY) = get_player_position()

#after
print(f"Play position: {coordX} {coordY}")
