"""
Instructions:
Make a program that asks the user for a word, then return to the user the
ceasar ciphered version of their word (encoded version)
Assume Cipher = 4
'a' : 'e'
'b' : 'f'
Also: asks for user input for cipher to select
and maybe encrypted and decrypt options
"""
i = 0
ciphered_word = [] # a list
ciphered_str = '' # a string
cipher4_alphabet = {
'a':'e',
'A' : 'E',
'b':'f',
'B' : 'F',
'c' : 'g',
'C' : 'G',
'd' : 'h',
'D' : 'H',
'e' : 'i',
'E' : 'I',
'f' : 'j',
'F' : 'J',
'g' : 'k',
'G' : 'K',
'h' : 'l',
'H' : 'L',
'i' :'m',
'I' : 'M',
'j' :'n',
'J': 'N',
'k' : 'o',
'K' : 'O',
'l' : 'p',
'L' : 'P',
'm' : 'q',
'M' : 'Q',
'n' :'r',
'N' : 'R',
'o':'s',
'O' : 'S',
'p':'t',
'P' : 'T',
'q':'u',
'Q' : 'U',
'r' :'v',
'R' : 'V',
's' :'w',
'S' : 'W',
'T' : 'X',
't' : 'x',
'u':'y',
'U' : 'Y',
'v':'z',
'V' : 'Z',
'w' :'a',
'W' : 'A',
'x' :'b',
'X' : 'B',
'y' :'c',
'Y' : 'C',
'z' : 'd',
'Z' : 'D',
' ' : ' ', #leaves spaces as they are to translate sentence
'.' : '.', # Other punctuation
',' : ',',
';' : ';',
'!' : '!',
}

cipher1_alphabet ={
        'a' : 'b',
        'A' : 'B',
        'b' : 'c',
        'B' : 'C',
        'c' : 'd',
        'C' : 'D',
        'D' : 'E',
        'd' : 'e',
        'E' : 'F',
        'e' : 'f',
        'g' : 'h',
        'G' : 'H',
        'I' : 'J',
        'i': 'j',
        'j' : 'k',
        'J' : 'K',
        'K' : 'L',
        'k' : 'l',
        'L' : 'M',
        'l' : 'm',
        'n' : 'o',
        'N' : 'O',
        'O' : 'P',
        'o' : 'p',
        'p' : 'q',
        'P' : 'Q',
        'Q':'R',
        'q' : 'r',
        'R' : 'S',
        'r' : 's',
        's' : 't',
        'S' : 'T',
        'T' : 'U',
        't' : 'u',
        'u' : 'v',
        'U' : 'V',
        'V' : 'W',
        'v' : 'w',
        'w' : 'x',
        'W' : 'X',
        'x' : 'y',
        'X' : 'Y',
        'Y' : 'Z',
        'y' : 'z',
        'Z' : 'A',
        'z' : 'a',
        ' ' : ' '
    }


while i > 0:
    word = input("Enter any word or sentence: \n")
    cipher = input("What cipher do you want to use? Choose either 1 or 4 \n")
    if cipher == '1':

        for letter in word: #goes through each letter in inputted word or sentence
            ciphered_word.append(cipher1_alphabet[letter]) #replaces each letter in the word with the corresponding value the letter's key in the ciphered alphabet is
            ciphered_str += str(cipher1_alphabet[letter])
        print(ciphered_str) #prints out the encrypted sentence
    elif cipher == '4':

        for letter in word: #goes through each letter in inputted word or sentence
            ciphered_word.append(cipher4_alphabet[letter]) #replaces each letter in the word with the corresponding value the letter's key in the ciphered alphabet is
            ciphered_str += str(cipher4_alphabet[letter]) #concatenates the letters to form words they represent
            print(ciphered_str) #prints out the encrypted sentence
        i += 1"""
    else:
        print("try again. Enter in 1 or 4 ")
        cipher = int(input("What cipher do you want to use? Choose either 1 or 4 \n")
"""
