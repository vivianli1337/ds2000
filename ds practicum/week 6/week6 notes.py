#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:47:20 2022

@author: vivian
notes:
    def my_function():
        function name has to be followed by (); can be empty or 
        parameters
        functions:  
            - shorten codes
        # body of function 
        print("Hello from a function")
    
    def main():
        - a function; call it as main
    - can see what function is defined & look at lines that are 
    not indented
    - see function and go to that function code
        
    or------
    if __name__ == "___main__":
        my_function() # no need for main()
    
    def my_addition(my_number):
        # my_number is the parameter
        m
        print or return result
        - my_addition(#must include a parameter)
    
    list comprehension:
- shortcut to creating a new list & running a loop
define:
    old_list = [1,2,3]
    new_list =[x for x in old_list]
same as ------
    new_list =[]
    for x in old_list:
        new_list.append(x)         

for & in - doing iteration
old_list = [1,3,5]
new_list = [x for x in old_list]
new_list 
[x+2 for x in old_list]
--> all value in list +2

return - ends loops & function
         
                      
    
"""
def my_function():
    print("Hello from my_function")
  
def my_addition(my_number):
    new_number = my_number + 10
    return new_number 
    

 
    
    
# def main():
#     my_function()
    
# main()    # see print("hello from my_function")
    
if __name__ == "__main__":
    my_function()
    print(my_addition(20))
    
    
    
    


