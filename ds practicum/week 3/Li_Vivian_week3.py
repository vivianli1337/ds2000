# -*- coding: utf-8 -*-
"""
DS 2001 Spring 2022 - LEE
Week 3 Assignment

@author: [Your Name and NU ID]
"""




"""
In this week's exercise, we are going to simulate one's retirement saving plan.
We will ask the user to supply the following information:
    (1) annual salary
    (2) percentage of salary invested in the stock market
    (the rest is saved in a "high yield" savings account that earns 0.5% annually)
    (3) their starting age
    (4) their planned retirement age
    
With the above information, we will compute the total amount of money the user
will have when they retire.





"""



def main():
    
    """
    Q1: Ask the user to supply:
        (1) annual salary (saved to variable named salary)
        (2) percentage invested in stock (saved to variable named percent_stock)
            e.g., if the answer is 30%, the user should enter 30.
        (3) starting age (saved to variable named start_age)
        (4) retirement age (saved to variable named retire_age)
    
    """
    
    salary = float(input("What is the annual salary?"))
    percent_stock = float(input("What percentage of salary was invested in stock?"))
    start_age = int(input("When did you start investing?"))
    retire_age = int(input("When do you plan to retire?"))
    
    """
    Q2: Print the values the user input on the screen
    
    """
    
    print("My annual salary is", salary)
    print("I have invested", str(percent_stock),"% in stock")
    print("I started investing at age", start_age)
    print("I plan to retire at", retire_age)

    
    """
    Q3: Compute the high yield savings account balance when the user retires.
        
        Some assumptions:
            
        **The annual percentage yield (apy) is 0.5%
        **The user receives their salary and saves & invest on 1/1
        **The user will earn compound interest annually on 12/31 
        **The user starts working on 1/1 of their starting age
        **The user retires on 12/31 of their retirement age
        **The user never withdraws
        
        Test case 1: salary = 100; invest 0% in stock; start age = 20; retire age = 20
                    => total saving when retired = $100.5
        Test case 2: salary = 100; invest 0% in stock; start age = 20; retire age = 21
                    => total saving when retired = $201.5025
        Test case 3: salary = 100; invest 20% in stock; start age = 20; retire age = 65
                    => total saving when retired = $4146.6931
    
    """
    
    apy = 0.005
    current_age = start_age
    total_saving = 0
    
    percent_stock = percent_stock/100
    
    percent_saving = 1 - percent_stock
    
    while current_age <= retire_age:
        saving_this_year = salary * percent_saving
        total_saving = (total_saving + saving_this_year) * (1 + apy)
        current_age = current_age + 1
    
    print("I can finally retire with", round(total_saving, 2))
  
    
    """
    Q4: Compute the investment account (stock) balance when the user retires.
    
        Some assumptions:
            
        **The stock market has good years, okay years, and bad years.
        **Annual return in a good year =   8%
                             okay year =   3%
                              bad year = -10%
        
        **Assume that the first year (the year the user starts saving) is always
        a good year, followed by an okay year, and then a bad year, and another
        good year, okay year, bad year (...). In other words, it's always
        good, okay, bad, good, okay, bad...etc.
    
        
        **Assume that the user invests on 1/1 every year
        **Assume that the stock market return is calculated on 12/31 every year
        **Assume that the user never sells
        
        
        
        Test case 1: salary = 100; invest 100% in stock; start age = 20; retire age = 20
                    => total stock when retired = $108
        Test case 2: salary = 100; invest 100% in stock; start age = 20; retire age = 21
                    => total stock when retired = $214.24
        Test case 3: salary = 100; invest 100% in stock; start age = 20; retire age = 22
                    => total stock when retired = $282.816
        Test case 4: salary = 100; invest 100% in stock; start age = 20; retire age = 23
                    => total stock when retired = $413.44128
        Test case 5: salary = 100; invest 70% in stock; start age = 20; retire age = 20
                    => total stock when retired = $75.6
        Test case 6: salary = 100; invest 40% in stock; start age = 20; retire age = 65
                    => total stock when retired = $1890.8038
    """     
    current_age = start_age
    total_stock = 0
    
     
    
    while current_age <= retire_age:
        if (current_age - start_age)%3 == 0:
            apy = 0.08
        
        elif (current_age - start_age)%3 == 1:
            apy = 0.03
            
        else:
            apy = -0.10
        
        total_investment = salary * percent_stock
        total_stock = (total_stock + total_investment ) * (1 + apy)
        current_age = current_age + 1
     
    print("I can finally retire with", round(total_stock, 2))


    
    """
    Q5: Compute and print the total net worth (savings +  investment)
        when the user retires.
        
        
        Test case 1: salary = 100; invest 30% in stock; start age = 20; retire age = 22
                    => total net worth when retired = $296.95 (saving = 212.11; stock = 84.84)
        Test case 2: salary = 50000; invest 70% in stock; start age = 20; retire age = 30
                    => total net worth when retired = $575735.52 (saving = 170033.43; stock = 405702.08)
    """
    
    total_net_worth = total_saving + total_stock
    
    print("the total net worth is $", round(total_net_worth, 2), "when the user retired")

    
        
    """
    Q6: Plot the year end total stock investment using plt.plot, display each point as
        a blue square ("bs") with markersize = 2. Specify the xlim as from two years
        before starting age until two years after retirement age
    """
    
    """
    we did not get to do #6 in class
    the coding below is my attempt at plotting it
    """
    import matplotlib.pyplot as plt
    plt.plot(current_age, total_stock, "bs", markersize = 2)
    plt.xlim(current_age - 2, retire_age + 2)
    
    current_age = current_age + 1
    
    plt.xlabel("Current Age")
    plt.ylabel("Total Stock")
    plt.title("Total Net Worth Saving")


    
main()

