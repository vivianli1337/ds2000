# -*- coding: utf-8 -*-
"""
Week 4 Assignment: Conditional, While-Loop, List, and File

@author: Vivian Shu Yi Li 
@NU ID: 001506227
"""




def main():
    
    """
    Q1: Conditional exercise
    
    Create a new variable called my_number. Initialize it to an integer.
    
    1. print my_number.
    2. If my_number is greater than or equal to 10, print "this number is
        greater than or equal to 10"
    3. If my_number is not greater than or equal to 10, then check if it's
        greater than 0. If it's greater than 0 AND it's also an odd number,
        print "It's an odd number between 0 and 10". If it's greater than 0
        AND it's an even number, print "It's an even number between 0 and 10."
    4. If my_number is less than or equal to 0, print "This number is less than
        or equal to 0"
    
    
    Initialize your my_number to different integers and make sure your conditionals
    print the correct message.
    
    """
    my_number = int(input("What is my number?"))
    
    if my_number >= 10:
        print("This number is greater than or equal to 10\n")
    
    else:
        if my_number > 0 and my_number%2 == 1:
            print("It's an odd number between 0 and 10\n")
        elif my_number > 0 and my_number%2 == 0:
            print("It's an even number between 0 and 10\n")
        else:
            print("This number is less than or equal to 0\n")
            
    """
    Q2: List exercise
    
    The variable my_list is defined below. (It's a list)
    Use the list slicing syntax to answer the following questions:


    https://www.geeksforgeeks.org/python-list-slicing/

                                        
    1. Write code to print the 1st element of the list                                    
    2. Write code to print the last element of the list
    3. write code to print the 1st, 3rd, 5th, 7th, 9th elements of the list
    4. Write code to print the 4th-7th elements of the list
    5. write code to print the 10th, 8th, 6th, 4th, 2nd, elements of the list.
    6. Write code to print the total number of elements in this list
    
    
    """
    my_list = [1,8,3,2,5,10,649,820,-3,-999]
    
    # 1st element
    print("The first element is", my_list[0])
    
    # last element
    print("The last element is", my_list[-1])
    
    # 1st, 3rd, 5th, 7th, 9th element
    print("The 1st, 3rd, 5th, 7th, and 9th elements are", my_list[::2])
    
    # 4th - 7th elements
    print("The 4th - 7th elements of the list are", my_list[3:7])
    
    # 10th, 8th, 6th, 4th, 2nd elements
    print("The 10th, 8th, 6th, 4th, and 2nd elements are", my_list[::-2])
    
    # total number of element
    print("The total number of elements is", len(my_list),"\n")
    
    
    """
    Q3: While loop exercise
    
    Mark is trying to save money for a house. He plans to save $1 on day 1, 
    $2 on day 2, ......, $100 on day 100, etc., into his savings account.
    The Back Bay property he plans to buy is priced at $1,500,000. Write a
    while-loop to determine on which day Mark will have enough money to buy
    the house. (You should create additional variables to help you keep
    track of the day and amount saved)
    
    """
    
    day = 0
    savings = 0
    
    while savings <= 1500000:
        day += 1
        savings = savings + day 
    
    print("Mark will have enough money ($1,500,000) to buy the house in", day, "days")
        
    
    
    """
    Q4: More list exercise
    
    
    Mark wants to know his account balance each day leading up to $1500000.
    Specify your while loop again, but this time also create a list to save
    each day's account balance in the list.
    
    Once the computation is completed:
        1. print day 1's account balance (it should be 1)
        2. print day 100's account balance (it should be 5050)
        2. print the last 10 elements of the list
        3. print every 100th element of the list (i.e., 1st, 101st, 201st,...)
       
    
    """
    day = 0
    savings = 0
    
    list_a = []
    
    while savings <= 1500000:
        day += 1
        savings = savings + day 
        
        list_a.append(savings)
        
    print(list_a, "\n")
    print("Mark will have enough money ($1,500,000) to buy the house in", day, "days\n")
    
    print("The account balance on day 1 is", list_a[0], "\n")
    print("The account balance on the 100th day is", list_a[99], "\n")
    print("The last 10 elements of the list are", list_a[-10:], "\n")
    print("The every 100th elements of the list are", list_a[::100], "\n")
    
   
    """
    Q5: File + list + loop exercise
    
    Read in Meta's stock price file ("meta_price.txt")
    Save each line of the txt file as an element to a list named meta_data
    Make sure you save each line as a float.
    
    
    You should keep reading new lines until the new line is empty, meaning you
    have reached the end of the file.
    
    
    Once the file is read completely into the list:
        1. print the total number of elements in the list
        2. compute Meta's average price
    
    
    """
    
    with open ("meta_price.txt", "r") as infile:
        meta_data = []
        
        while True:
            each_line = infile.readline().strip()
            
            if each_line == "":
                break
            
            meta_data.append(float(each_line))
            
        print("The total number of elements in the list is", len(meta_data), "\n")
        print("The average price is", sum(meta_data)/len(meta_data))
    

main()
