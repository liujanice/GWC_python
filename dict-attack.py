import enchant

d = enchant.Dict("en_US") #variable 'd' is set to english dictionary


# >>> d.check("Hello")
# True
# >>> d.check("Helo")
# False
# d.suggest("Helo")
# ['He lo, 'He-lo', 'Hello', 'Helot', 'Help', 'Halo', 'Hell', 'Held']

#Part 1: Write a program that will alert a user if a password that they entered
# is a real word, thus making it suspectible to a dictionary attack

times = 1
current_year = input("Type in the current year\n")
while times > 0:
    birth_Date = input("Enter in your birthday in monthdayyear. For example: 05231999\n")
    if len(birth_Date) == 8:
        print("Great.")
        times -= 2
    else:
        print("Try again. Remember to enter in integers only")
        birth_Date = input("Enter in your birthday in monthdayyear. For example: 052399")

demographics = [current_year, birth_Date]

def variations(word):

    word = word.replace("l", "1")
    return(word)
    word = word.replace("i", "1")
    return(word)
    word = word.replace("i", "!")
    return(word)


user_password = input("Now, enter in a password \n")
user_password = user_password.lower()
password = [user_password]
d.check(user_password)
if d.check(user_password) == True:
    print("Your password is too weak! Enter in a stronger password")
elif d.check(user_password) == False:
    for element in demographics:
        if element in user_password:
            print("Your password is too weak. Never use your birthday nor the current year in your password")


#Part 2
    word = user_password

    #recheck(word)
    word = word.replace("@", "a")

    word = word.replace("4", "a")

    word = word.replace("3", "e")

    word = word.replace("1", "l")

    word = word.replace ("5", "s")
    word = word.replace ("$", "s")

    word = word.replace ("6", "b")

    word = word.replace ("8", "b")

    word = word.replace ("9", "g")

    word = word.replace ("2", "z")
    word = word.replace("!", "i")

    word = word.replace ("0","o")
d.check(word)
if d.check(word) == True:
    print("Your password is similar to the word:", word)
    print("It is weak")
else:
    word = word.replace("1", "i")
    print("Your password is similar to the word:", word)
    print("It is weak")

print("Other similar words to your password are:")

print(d.suggest(word))
print(variations(word))
print("The above are not wise choices to use as a password")
    #variations(word)# later for making function that creates all variations
print("Make your password stronger by adding random symbols in addition to numbers that could be references to multple things that will make your password incoherent to everyone else but you")
