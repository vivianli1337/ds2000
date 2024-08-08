#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
class notes 

@author: vivian
for loop:
    1. iteration by value
    2. iteration by position
    - list of things that you want to iterate through
    - want to loop for a number of time
    
    lst= ['first', 'second', 'third']
    for element in lst: 
        print(element)
    iteration by value bc each time, the element 
    take the element from the list
    - value
    
    a = [1,2,3]
    a[0] - first element
    each element has a position
    for i in range(len(lst)):
        print(lst[i])
        - if i = 0 --> the first position
        - if i = 1 --> the second position
        - if i = 2 --> the thrid position
        
    len(a) = 3 - number of element
    range(3) - range (0,3) tell the starting point of position 0 with a
    exclusive point of position 3
    - sequence of integers
    
    can replace:
        ***** len = total number of elements***
    for i in range(len([['first', 'second', 'third']])):
    for i in range(3):
    for i in range(0,3):
    for i in [0,1,2]:
        print(lst[i])
    iteration by position    
    - specific index
    
    
    
    
    
    b = [[1,2,3], [4,5,6]]
    b[0] = [1,2,3]
    b[1] = [4,5,6]
    b[0][0] = 1
    - the fist [] indicate the first element
    - the second [] indicate the first position in the first element\
        
    i = temperory variable
    
    split = makes new list for strings only
    "hello you". split()
    ['hello', 'you']
    
    
    "hello you - hi".split("-")
    use dash to split
    ['hello you', 'hi']
    
    when in string, all letter is considered
    "company"[:3]
    'com'
    all strings are like list w/ all letters
    
    
"""

def main():
    lst= ['first', 'second', 'third']
    for element in lst: 
        print(element)
    
    for i in range(len(lst)):
        print(lst[i])
main()