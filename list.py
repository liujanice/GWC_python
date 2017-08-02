groceries = ["chips", "bagels", "bread", "crackers","pasta", "pizza", "ice cream", "soda",
"bbq sauce", "cake", "peaches", "bananas","muffins"]

# extend and append are functions
groceries.extend(["eggs", 'noodles'])
#Extend only MERGES ANOTHER LIST into the previous list.
groceries.append("bacon")
#Append adds a SINGLE item only to a list. Thus, what is in the parentheses is treated like ONE ITEM

forgotten = ["onions", "ginger", "broccoli", "potatos", "tea", "coffee beans",
"rice", "peanuts", "dried apricot", "mangos", "milk"]


print("I bought these today:")
# iterates through the groceries list
for item in groceries:
    print(item)
# Asking for user input to find an item they forgot by using that value as the index in the list
answer = int(input("oh no! What else do I need to buy? Enter in an integer from 0 to 10: "))

#If the user's input is within the range of the indexes of the forgotten list, then
# the program will print out the item
if answer >= 0 and answer <= 10:
    print()
    print(forgotten[answer])
    # If not, there are no items that were forgotten
else:
    print("Nevermind. I think I bought everything I need.")
