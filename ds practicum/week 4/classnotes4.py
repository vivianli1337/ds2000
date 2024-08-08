#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:50:27 2022

@author: vivian

a_list = [1, 2, 3]
must be in []; "," separate elements
- have access to any element
- start with position 0 = the first element

a_list[0] - for specific element

b_list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

to find last element: b_list[-1] 
- position starting from the end of the list
- could also use b_list[9]

to find second to last element: b_list[-2]
- or b_list[8]

c_list = ["hi", "hey", "hello"]
c_list[0] = "hi"
c_list[-1] = "hello"

can mix different type of values together:
d_list[1, "hey", 3.355]

first 3 elements: list slicing; use ":"
before the colon is the beginning; after the colon 
is the ending number which is excluded

b_list[0:2] - elements from the first element 
to the second element
b_list[1:5] = [2, 3, 4, 5] there is no 6

to skip- use "::"
- first is the beginning, second is the end (excluded),
third is the skip positions - sequence
b_list[0:6:2] = [1, 3, 5] - increment by 2 positions

b_list[2:] - no number after ":" means to the end
- from 2 all the way to the end

b_list[:4] - no number before ":" means starting 
from the beginning

test_list = [1,2,3,4,5,6,7]
test_list[0] - first element
test_list[-1] - last element
test_list[1:3] - 2nd and 3rd elements
test_list[::2] - from the beginning to the end with a skip of 2
test_list[::-1] - skip is 1 but backward; reverse
- [7,6,5,4,3,2,1] - starting from right hand side

len(list_b) = total elements in list_b


"""

def main():

    
main()