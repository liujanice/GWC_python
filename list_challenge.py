#Starter code for List Challenge Activity
random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71,
84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45,
85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43,
99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]

#Level 1: find and print all multiples of 5 in the list
"""
for number in random_numbers:
    if number%5 ==0:
        print(number) #displays the integers that are multiples of 5 in the list
"""

#Level 2: find the sum of all multiples of 3 and 5 in the list
"""
sum1 = 0
for number in random_numbers:
    if number%3 ==0 or number%5 ==0: # '%'means module and finds the remainder in the division
        sum1 = sum1 + number #continues to add each number that is either a multiple of 5 or 3 to the overall sum
print(sum1)
"""

#Level 3: find the sum of all the prime numbers in the list
sum1 = 0

for number in random_numbers:
    Prime = True #boolean called prime
    for integer in range(2, number):
        #if it's not prime, then set Prime = false
        if number % integer == 0:
            Prime = False #Not a prime
    if Prime == True:
        print(number)
        sum1 = sum1 + number
print(sum1)
