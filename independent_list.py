
from random import *


#Create the list of words you want to choose from.
name_list = ["Rena", "Iris", "Tom"]
last_name_list = ["Lee", "Brighton","Currin", "Kingsley", "Fallon"]

#Create a variable to play this again
play = 0

while play < 1:
#Generates a random integer.
    x = randint(0, len(name_list)-1)
    y = randint (0, len(last_name_list)-1)
    print (name_list[x] , last_name_list[y])
    play = play + 1
    retry = str(input("Do you want to play again? Enter 'Yes' to play again and 'No' to exit \n"))
    if retry == 'Yes':
        play = 0
    else:
        play = 3
