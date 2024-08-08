#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:17:51 2022

@author: vivian
"""

"""
lesson:
 # string concatenation
 s = "hello"
 t = "world"
 word = s + " " + t
 print(word) # print "hello world"
 
 # replication
 times = s * 3
 print(times) #hellohellohello 
 # cannot do subtraction or division ==> type error
 
 # compare:
 "grizz" > "asteroid" # true
 # look at character by character
 # compare the first letter and see which one is greater
 # every letter is associated w/ value (ASCII value - use ord(""))
 
 #capital letter have smaller value bc they come first before lowercase
 "G" > "a" # false
 
 
 # iterate by value -> print individual letters one by one
 r = "Reddit"
 for letter in r:
     print(letter)
 # string positionins and slicing to get substrings
 r[:3] # Red
 r[4:] # it
 r[1:3] # edd
 
 # split turns strings into list
 # join turn list into string
 letters = ["h", "e", "l", "l", "o"]
 word = "".join(letters)
 #hello
 word = "-".join(letters)
 #h-e-l-l-o
 word = "!".join(letters)
 #h!e!l!l!o
 
 
 date = "march 22nd"
 #iterate by value
 for letter in date:
     print(letter)
 date[0] # return "m"
 months = ["march", "april"]
 for month in months:
     for letter in month:
         print(letter)
         
 "list of words".split #change to list     
 "".join(months) # one string
 
 s = "hello"
 s[1:] # ello
 #iterate by position
 for i in range(len(date)):
     print(date[i])
 
 
 # try it w/ string function
 # cannot modify string
 # must make new variable to save modification
 r = "Reddit"
 r1 = r.replace("Red","Rea")
 r_l = r.lower()
 r_u = r.upper()
 # function ask if the word contains all alphabetic
 r_a = r.isalpha()
 
 dog = "grizz"
 cat = "asteroid"
 
 dog2 = dog.replace("z", "Z")
 print(dog2)
 # identify if data is not words --> clean up data
 dog3 = dog.isalpha()
 print(dog3)
 "??".isalpha() #false
 "!".isalpha() #false
 
"""



"""
cleaning a string:
    1. remove punctuation
    2. turn everything lowercase
    
    
example:
    input = "Hey Grizz! Put that down..."
    output = "hey grizz put that down"
"""


def clean_string(input_st):
    """ function clean_string
        parameter: input string, a string
        returns: cleaned up version of a string
    """
    output_str = ""
    for letter in input_st:
        if letter.isalpha() or letter == " ":
            output_str += letter.lower()
    return output_str
            
            
def main():
    string = input("Enter a sentence...|n")
    cleaned = clean_string(string)
    print("Cleaned version", cleaned)

   
main()
