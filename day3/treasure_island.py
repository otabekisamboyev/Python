print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island! Your mission is to find the Treasure!")
direction = input("You are at a crossroad, where do you want to go? Type 'Left' or 'Right' ")
if direction.lower() == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. "
                   "Type 'Wait' to wait for a boat. Type 'Swim' to swim across")
    if action.lower() == "swim":
        print("You got attacked by an angry trout. Game over!")
    elif action.lower() == "wait":
        door = input("You arrive at the island unharmed. There is an house with 3 doors."
                     " One red, one blue and one yellow. Which color do you chose? ")
        if door.lower() == "red":
            print("It's room full of fire. Game over!")
        elif door.lower() == "blue":
            print("You enter a room of beasts. Game over!")
        elif door.lower() == "yellow":
            print("You found the Treasure. You win!")
        else:
            print("Wrong insert!")
    else:
        print("Wrong insert!")
elif direction.lower() == "right":
    print("You fell into a hole. Game over!")
else:
    print("Wrong insert!")
