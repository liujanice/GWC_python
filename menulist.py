from random import *

order = 0

while order < 1:
    print("What would you like to order?")


#Create the list of words you want to choose from.
    entree = ["Potato Salad","Lasagna", "Ramen", "Pasta"]
    appetizer = ["Potato Sliders" , "Fried Ravioli", "Wonton Cups",
    "French Fries"]
    desserts = ["Cheesecake", "Ice Cream", "Snickerdoodle",
    "Double Chocolate Chip Cookie"]


#Generates a random integer.
    x = randint(0, len(entree)-1)
    y = randint (0, len(appetizer)-1)
    z = randint (0, len(desserts)-1)

    print("I would like to order: " + entree[x] + ", " + appetizer[y] +
    ",and " + desserts[z])
    order += 1
    retry = input("Anything else? Enter 'y' to continue to add onto your order and 'n' to finish)\n")
    if retry == 'y':
        order = 0
    if retry == 'n':
        order = 2
