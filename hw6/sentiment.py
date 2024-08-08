#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Vivian Shu Yi Li
 DS 2000
 Spring 2022
 HW6
 March 26, 2022
 sentiment.py
"""
REDDIT = "reddit.txt"

POSITIVE = ["good", "happy", "relieved", "relief", "glad",
            "finally", "normal", "excited", "proud", "well",
            "healthy", "lol", "great", "reduce", "recovering", "resources",
            "care", "amazing", "successful", "encourage", "great",
            "supports", "support", "better", "incredibly", "efficient",
            "under control", "reduce", "effective", "reduce", "vaccine"]

NEGATIVE = ["bad", "angry", "frustrated", "stressed", "stupid",
            "scary", "scaring", "afraid", "hate", "hated", "annoying", 
            "annoyed", "tired", "disappointing", "lol", "covid", "hate",
            "covid", "complain", "failing", "unfairly", "lack", "disease",
            "severe", "deaths", "scared"]

import matplotlib.pyplot as plt

def read_file(filename):
    """function read_file
    parameter: filename, rows of words in strings
    return: a list of comments
    """
    comments = []
    with open(filename, "r", encoding = "utf-8") as infile:
        while True:
            neu = infile.readline()
            username = infile.readline()
            points = infile.readline()
            timestamp = infile.readline()
            comment = infile.readline()
            blank = infile.readline()
            if not comment:
                break
            
            comments.append(comment)
    return comments        

def clean_com(input_com):
    """ function: clean_com
    parameter: input comment, a string
    return: cleaned version of a string
    """
    output_com = ""
    for words in input_com:
        if words.isalpha() or words == " ":
            output_com += words.lower()
    return output_com      

def sentiment_score(comment, pos, neg):
    """ function: sentiment_score
    parameter: comment (strings), list of pos words, list of neg words
    return: average sentiment score (float between -1 and +1)
    """
    score = 0
    words = comment.split()
    for word in words:
        if word in pos:
            score += 1
        if word in neg:
            score -= 1
    return score / len(words)

def plot_graph(dic1, dic2, dic3):
    """ function plot_graph
    parameter: dictionaries
    return: nothing; just plot a graph
    """
    
    plt.plot(dic1.keys(), dic1.values(), "o", color = "midnightblue", 
             markersize = 5, label = "neutral")
    plt.plot(dic2.keys(), dic2.values(), "o", color = "lightskyblue", 
             markersize = 5, label = "positive")
    plt.plot(dic3.keys(), dic3.values(), "o", color = "lightpink", 
             markersize = 5, label = "negative")
    
    # label
    plt.title("The Average of Reddit Comments' Sentiment Scores")
    plt.xlabel("Position in List")
    plt.ylabel("Sentiment Score")
    plt.legend(loc = "lower right")
    plt.show()
    
def main():
    # step 1: gather the info - read from the file
    comment = read_file(REDDIT) 
    
    # step 2: computation; find all sentiment scores for each comment using 
    # call function sentiment_score and add them into the list
    senti_score_list = []
    for line in comment:
        cleaned = clean_com(line)
        senti_score = sentiment_score(cleaned, POSITIVE, NEGATIVE)
        senti_score_list.append(senti_score)
        senti_score_list.reverse()
    
    # create a dictionaries of individual categories
    positive = {}
    negative = {}
    neutral = {}
    
    # add the scores into their appropriate dictionary
    for i in range(len(senti_score_list)):
        if senti_score_list[i] == 0:
            neutral[i] = senti_score_list[i]
        elif senti_score_list[i] < 0:
            negative[i] = senti_score_list[i]  
        elif senti_score_list[i] > 0:
            positive[i] = senti_score_list[i]
    
    # find the overall average score
    average = sum(senti_score_list)/len(senti_score_list)
    
    #step 3: communicate    
    print("The overall average sentiment score:", average)
    if average < 0:
        print("The community has been more worried in the last few months.")
    if average > 0:  
        print("The community has been more calm in the last few months.")
        
    # plot the sentiment scores using the call function
    plot_graph(neutral, positive, negative)
    
main()