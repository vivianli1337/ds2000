#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:26:52 2022

@author: vivian
"""
NEU_FILE = "neu_announcements.txt"

def read_txt(filename):
    """ function read_txt
    parameter: filename, a string
    return: word count, dictionary
    """
    wordcount = {}
    with open(filename, "r") as infile:
        while True:
            word = infile.readline()
            if word == "":
                break 
            word = word.strip()
            if word in wordcount:
                wordcount[word] += 1
        
        # new work = see it once
        # reminder that [] is use to add element in dictionary
            else:
                wordcount[word] = 1
    
    return wordcount
            
def find_max_word(count_dct):
    """function find_max_word
    parameter: dictionary where key - string and value (frquency/occurence tied to)
    return: tuple of (key, value)
    """
    max_key = ""
    max_value = -1
    
    for key, value in count_dct.items():
        if value > max_value:
            max_value = value
            max_key = key
        return (max_key, max_value)
        
def main():
    # step 1: gather dad from the file
    wc = read_txt(NEU_FILE)

    # step 2: computation
    # find out the common word in the file
    word, frequency = find_max_word(wc)
    
    # step 3: communication
    print("the most frequent word in the announcement was",
          word, "which was written", frequency, "times.")
    
    word = input("Which word to find out?\n")
    freq = wc[word]
    print("That was said", freq, "times")
    
main()
    
