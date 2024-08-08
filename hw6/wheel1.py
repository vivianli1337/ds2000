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

def letters(phrase):
    letter_counts = {}
    for words in phrase:
        for c_letters in words:
            if c_letters in letter_counts.keys():
                letter_counts[c_letters] += 1
            else:
                letter_counts[c_letters] = 1
    return letter_counts

def common_letter(letters, number, word):
    """ function common_letter
    parameter: a dictionary of letters and count
    return: the max count of letter (common letter) in dictionary
    """
    common_letters = {}
    while len(common_letters) < number:
        max_count = 0
        max_letter = ""
        for key, value in letters.items():
            if key in word and key not in common_letters.keys():
                if value > max_count:
                    max_count = value
                    max_letter, max_count = key, value
                    
        common_letters[max_letter] = max_count
    
    return common_letter

def show_puzzle(ran_word, revealed_word):
    """ function show_puzzle
    parameter: common vowels and consonants from a random string
    return: blank line that is not revealed
    """
    for letter in ran_word:
        if letter not in revealed_word:
            print("__ ", end = " ")
        else:
            print(letter, end = " ")
            
def main():
    wheel_words = read_file(PUZZLE)
    
    random_word = random.choice(wheel_words) 
    # finding the frequencies
    counts = []
    counts = letters(wheel_words)
   
    com_vowels = []
    com_consonants = []
   
    com_vowels = common_letter(counts, 1, VOWELS)
    com_consonants = common_letter(counts, 3, CONSONANTS)
    
    revealed = ["R", "S", "T", "L", "N", "E"]
    
    
    
    print("Automatically showing:", revealed)
    show_puzzle(random_word, revealed)
    
    print(com_vowels.keys())
    print(com_consonants.keys())
    
   # cheating = list(com_vowels.keys()) + list(com_consonants.keys()) + revealed
    
   # print("Based on the letter counts Vanna is revealing 3 more consonants, and one more vowel...")
    
   # show_puzzle(random_word, cheating)
   # user_guess = input("Enter your guess, including all spaces and punctuations")
   # user_guess = user_guess.upper()
    
   # if random_word == user_guess:
    #    print("Congrats! You won!")
   # else:
  #      print("Sorry, you lose. Try again!")
main()