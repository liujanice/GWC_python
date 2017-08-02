"""
Instructions:
Make a program that asks the user for a word, then return to the user the
ceasar ciphered version of their word (encoded version)
Assume Cipher = 4
'a' : 'e'
'b' : 'f'
"""
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
word = input("Enter any word or sentence: \n")
for letter in word: #goes through each letter in inputted word or sentence
    ciphered_word.append(cipher4_alphabet[letter]) #replaces each letter in the word with the corresponding value the letter's key in the ciphered alphabet is
    ciphered_str += str(cipher4_alphabet[letter]) #concatenates the letters to form words they represent
print("Encoding is:")
print(ciphered_str)#prints out the encrypted sentence
