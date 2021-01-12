#!/bin/python

print ("Vigenere Decypher\n")
print ("Text must be entered without Symbols or Space\n")

plain = raw_input("Enter Known Text: ")
encrypted = raw_input("Enter the corresponding Encrypted text to the known text: ")
password = ""

for i in range(len(plain)):
    x = ((ord(encrypted[i]) - ord(plain[i])) % 26) + 97
    char = chr(x)
    password = password + char

print password
