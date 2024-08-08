#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vivian Shu Yi Li
DS 2000
Spring 2022
HW6
April 1, 2022
wheel.py
"""

import random
PUZZLE = "puzz.txt"

CONSONANTS = ["B", "C", "D", "F", "G", "H", "J", "K", "M", "P", "Q", 
              "V", "W", "X", "Y", "Z"]
VOWELS = ["A", "I", "O", "U"]

def read_file(filename):
    """ function read_file
    parameter: open a file & read each line
    return: a list of all the words in string
    """
    phrase = []
    with open(filename, "r") as infile:
        while True:
            puzzles = infile.readline()
            puzzles = puzzles.strip().upper()
            if not puzzles:
                break
            phrase.append(puzzles)   
    return phrase  

def letters_count(lst):
    """ function letters_count
    parameter: a list of words
    return: a dictionary of letter count
    """
    letter_c = {}

    for word in lst:
        for letter in word:
            if letter in letter_c.keys():
                letter_c[letter] += 1
            elif letter not in letter_c.keys():
                letter_c[letter] = 1
    return letter_c

def common_letter(letter_c, letters_dict, number):
    """ function common_letter
    parameter: a dictionary of letters and count
    return: the max count of letter (common letter) in dictionary
    """
    common_dict = {}
   
    while len(common_dict) < number:
        letter_value = 0
        max_letter = ""
        for letter, count in letter_c.items():
            if letter in letters_dict and letter not in common_dict.keys():
                if count > letter_value:
                    letter_value = count
                    max_letter, count_max = letter, count
        common_dict[max_letter] = count_max
    return common_dict


def show_puzzle(random_word, revealed):
    """ function show_puzzle
    parameter: show given letters
    return: nothing; just show the blank lines and revealed letters
    """
    for letter in random_word:
        if letter not in revealed:
            print("__ ", end = " ")
        else: 
            print(letter, end = " ")
        
def main():
    # Step 1: get info from the file
    wheel_words = read_file(PUZZLE)
    
    # add all the letter counts of phrases into a new list
    count = []
    count = letters_count(wheel_words)
    
    # step 2: computation; find 3 most common consonants and most common 
    # vowel --> add into the new list
    common_vowels =[]
    common_consonants = []
    common_consonants = common_letter(count, CONSONANTS, 3)
    common_vowels = common_letter(count, VOWELS, 1) 
    
    # step 3: communicate; choose a random phrase and revealed the 
    # given letters also give some cheat-letters
    random_word = random.choice(wheel_words)
    revealed = ['R', 'S', 'T', 'L', 'N', 'E'] 
    print("Automatically Showing: R, S, T, L, N, E")
    show_puzzle(random_word, revealed)
    
    cheating = list(common_vowels.keys()) + list(common_consonants.keys()) \
        + revealed
    print("Based on the letter counts, Vanna is revealing 3 more"
          "consonants,and one more vowel...")
    show_puzzle(random_word, cheating)
    
    # let the user insert their guess & show result
    user_guess = input("Enter your guess, including spaces and punctuation.\n")
    user_guess = user_guess.upper()
   
    if random_word == user_guess:
        print("CCongrats! YOU WON!")
    else:
        print("Sorry! You lose...The puzzle was:", random_word, "Try again!")
              
        
        
    
    
    
    
    
    
    
    
    
main()
    