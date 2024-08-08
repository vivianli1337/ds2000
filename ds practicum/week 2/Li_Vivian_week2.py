# -*- coding: utf-8 -*-
"""
DS2001 (S22-LEE) Week 2 Assignment

Rename this file as Lastname_Firstname_week2.py
Submit the completed file to Canvas.


@author: [Vivian Shu Yi Li]
"""


def main():
    '''
    Grocery Bill
    
    You are going to build a calculator to calculate grocery bills.
    
    Q1:
    This calculator should ask for the user's name using the input() function.
    The user name should be saved to a variable called 'name'. Make sure to
    provide an informative prompt so your user knows to input their name.
    '''
    
    name = input("What is your name?")
    print(name)
    
    
    

    '''
    Q2:
    
    Now that you have the user name saved, display the following greeting:
    "Hi [name]!". Make sure to print it on the screen so your user sees it. 
    
    
    
    '''
    print("Hi",name,"!")
    
    
    
    
    
    
    
    
    '''
    Q3:
        
    Let's assume the user buys chips, soda, and broccoli. In a series of
    questions, ask your user to input how many bags of chips, how many cans of
    soda, and how many pounds of broccoli they want. Make sure to save the
    quantities to different variables.
          
    
    '''
    PRODUCT_PRICE = "product_price.txt"
    
    chips =  int(input("How many bags of chip?"))
    soda = int(input("How many cans of soda?"))
    broccoli = float(input("How many pounds of broccoli they want?"))


    '''
    Q4:
    
    The file named "produce_price.txt" contains the unit prices of chips
    (line 1), soda (line 2), and broccoli (line 3). Open the file and read
    these prices into 3 different variables (p_chips, p_soda, p_broccoli).
    '''
    PRODUCT_PRICE = "product_price.txt"
     
    with open(PRODUCT_PRICE, "r") as infile:
        p_chips = float(infile.readline())
        p_soda = float(infile.readline())
        p_broccoli = float(infile.readline())
        


    '''
    Q5:
        
    Compute the grocery bill for you user by multipling unit price by quantity,
    and add everything up. This is the bill before discount. Print the amount
    on the screen.
    
    '''
    total = chips * p_chips + soda * p_soda + broccoli * p_broccoli
    
    print(total)

     
    '''
    Q6:
    
    Your user might be getting a discount. Ask the user to input the discount
    amount. Provide an informative prompt to instruct them how to input the 
    percent off. (E.g., if they are getting 20% off, ask them to type 20.)
    
    Once the user provides the discount percentage, compute and print the
    final bill on the screen.
    
    

    Make sure your grocery calculator is working properly by checking
    the following test cases:
        (1) 1 bag of chips, 1 can of soda, 1 lb of broccoli, 10% off:
            pre-discount bill = $7.17, final bill = $6.453
        (2) 2 bags of chips, 3 cans of soda, 2 lbs of broccoli, 20% off:
            pre-discount bill = $15.33, final bill = $12.264. 

    
    '''
    
    discount = int(input("discount amount"))
    
    print(round(total * (1- discount/100), 2))
    
    


    
    '''
    Q7:
        
    Dogecoin calculator. The file 'dogecoin.txt' has four lines that correspond
    to the price (in $) of Dogecoin on 5/1/2021, 6/1/2021, 7/1/2021, and 8/1/2021,
    respectively. E.g., 1 Dogecoin = $0.339 on 5/1/2021.
    
    You bought $10 worth of Dogecoin on 5/1/2021, another $10 on 6/1, and yet
    another $10 on 7/1. On 8/1 you sold all your Dogecoin.
    
    You should read the lines of the file to do the computation. You should compute
    and print 3 things:
        (1) What's the amount of Dogecoin you held on 8/1 before selling?
        (2) How much $ did you have after selling all your Dogecoin on 8/1?
        (3) Use this formula to compute and print your rate of return:
            rate of return = (final_investment_value - total_cost)/total_cost 
    
    '''
    DOGECOIN = "dogecoin.txt"
    
    dogecoin_m = float(input("What is the amount of dogecoin in may?"))
    dogecoin_j = float(input("What is the amount of dogecoin in june?"))
    dogecoin_ju = float(input("What is the amount of dogecoin in july?")) 
    
    
    with open(DOGECOIN, "r") as infile:
        p_may = float(infile.readline())
        p_june = float(infile.readline())
        p_july = float(infile.readline())
        p_aug = float(infile.readline())
        
    total_amount = (dogecoin_m / p_may) + (dogecoin_j / p_june) + (dogecoin_ju / p_july)
    
    print("Amount of Dogecoin hold on 8/1 before selling is", total_amount)
    
    total_dollar = total_amount * p_aug
    
    print("Dollar after selling dogecoin", total_dollar)
    
    print("Rate of return is:", (total_dollar - 30) / 30)
    
    
        
   
    
    
    
    
    
    
    
        
                 
               
    
    
    




main()



