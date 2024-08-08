#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:29:22 2022

@author: vivian
"""
import random

REDDIT = "reddit.txt"

POSITIVE = ["good", "happy", "relieved", "relief", "glad",
            "finally", "normal", "excited", "proud", "well",
            "healthy", "lol", "great"]

NEGATIVE = ["bad", "angry", "frustrated", "stressed", "stupid",
            "scary", "scaring", "afraid", "hate", "hated", "annoying", 
            "annoyed", "tired", "disappointing", "lol"]



def sentiment_score(comment, pos, neg):
    """ function: sentiment_score
    parameter: comment (a string), list of pos words, list of neg words
    return: sentiment score (float between -1 and +1)
    """
    score = 0
    words = comment.split()
    for word in words:
        if word in pos:
            score += 1
        if word in neg:
            score -= 1
    return score / len(words)

def read_comments(filename):
    """function read_comment:
        parameter: filename, string
        return: list of strings, one per linne in the file
    """
    comments = []
    with open(filename, "r", encoding = "utf-8") as infile:
        while True:
            comment = infile.readline()
            if not comment:
                break
            comments.append(comment)
    return comments
    
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
    #string = input("Enter a sentence... \n")
    #cleaned = clean_string(string)
    #print("Cleaned version", cleaned)
    
    #step one: read data from the file, and comment per
    # element in a list
    comments = read_comments(REDDIT)
    
    # steo two: computation - clean up the one random comments
    # to remove punctuation/numbers and make it all lowercase
    comment = random.choice(comments)
    clean = clean_string(comment)
    score = sentiment_score(clean, POSITIVE, NEGATIVE)
    
    #step 3 communication - print the cleaned up comment and its score
    print(clean)
    print("Sentiment score:", score)
    

main()