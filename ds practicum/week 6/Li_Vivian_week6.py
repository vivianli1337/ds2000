### Week 6 Exercise

# DATA is a list of lists, where each element contains a
# company_name, CEO name, and EPS_2018 (annual diluted earnings per share)

DATA=[['Alphabet','Sundar Pichai', 43.7],
 ['Amazon','Jeff Bezos',20.14],
 ['Apple','Tim Cook', 11.91],
 ['Coca-Cola','James Quincey',1.5],
 ['Gap','Robert Fisher',2.14],
 ['Microsoft','Satya Nadella',2.13],
 ['Tesla','Elon Musk',-5.72],
 ['Twitter','Jack Dorsey',1.56],
 ['Uber','Dara Khosrowshahi',2.08],
 ['Facebook', 'Mark Zuckerberg', 7.57]]





"""
Q1:
    
    Write a function called greet_print. This function
    should take a string as parameter. Let's
    name this parameter your_name. This function should
    print a string: "Hi your_name", where your_name is 
    the parameter value specified by the user.
    
"""

def greet_print(your_name):
    """ function great_print
    parameter: a string asking for name
    returns: none
    """
    
    print("Hi", your_name)

"""
prof: print("Hi " + your_name)
"""

"""
Q2:
    
    Write a function called greet_return. This
    function should take a string as parameter. Let's
    name this parameter your_name. This function should
    return a string as output. Specifically,
    the return value should be "Hello your_name", where your_name
    is the parameter value specified by the user.
"""

def greet_return(your_name):
    """ function greet_return
    parameter: string asking for name
    returnL print: your name
    """
    your_name = "Hello" + " " + your_name
    return your_name


"""
Q3:
    Write a function called times5. This function should 
    take a float as parameter. Let's name this parameter
    this_number. This function should return a float as output.
    Specifically, the return value should be this_number x 5.


"""

def times5(this_number):
    """ function times5
    paramter: this number - float
    return: float - number
    """
    this_number = this_number * 5
    return this_number


"""
Q4:
    Write a function called isEven. This function should
    take an integer as parameter. Let's name this parameter
    this_integer. This function should return True if 
    this_integer is an even number and return False if
    this_integer is an odd number.

"""

def isEven(this_integer):
    """ function isEven
    parameter: number - integer
    return: True if even; false if odd
    """
    if this_integer % 2 == 0:
        return True
    else:
        return False
        

"""
Q5:
    Write a function called company_eps_5. This function takes 
    no parameter. It should first create an empty list called
    eps5_list. Then it will use a for-loop to iterate over the
    DATA constant (the list of list defined at the beginning
    of this file) to append the names of companies whose EPS
    is >=5.0 to eps5_list.
    
    The return value of this function should be your eps5_list.
    Before returning the list, modify your list such that each
    element only contains the first 3 letters of each company's
    name in upper case.
    
       

    Hint 1: You can access individual letters of a string as if
            they were a list of letters
    Hint 2: You can use string's upper() function to convert letters
            to uppercase

"""
def company_eps_5():
    """ function company_eps_5
    parameter: empty list
    return: eps5_list - list of companys with first 3 in uppercase
    """
    eps5_list = []
    for i in DATA:
        EPS = i[2]
        if EPS >= 5.0:
            eps5_list.append((i[0][:3]).upper())
    return eps5_list
    
"""
prof:
    eps5_list = []
    for a_company in DATA:
        if a_company[2] >= 5:
            eps5_list.append(a_company[0][:3].upper())
    return eps5_list
"""

"""
Q6:
    Write a function called reverseAnd10x_forloop. This function
    should take a list of floats as parameter. Let's name this
    parameter this_list. This function should reverse the elements
    in this_list and use a for loop to multiply each element by
    10. Finally, the function should return the new list.
"""

def reverseAnd10x_forloop(this_list):
    """function reverseAnd10x_forloop
    parameter: list of floats
    return: new list where elements are reversed
    """
    list_reversed = this_list[::-1]
    
    new_list = []
    
    for i in list_reversed:
        new_list.append(i*10)
        
    return new_list 
    



"""
Q7:
    Write a function called reverseAnd10x_listcomp. This function
    should take a list of floats as parameter. Let's name this
    parameter this_list. This function should use list comprehension
    to reverse the elements in this_list and multiply each element by
    10. Finally, the function should return the new list.
"""
def reverseAnd10x_listcomp(this_list):
    """ function reverseAnd10x_listcomp
    parameter: this_list - float
    return: new list that is reversed & elements * 10
    """
    reversed_list = this_list[::-1]
    final_list = [i*10 for i in reversed_list]
    return final_list
    
   
    """
    prof: 
    final_list = [i*10 for i in this_list[::-1]]
    return final_list
    """








"""

Below is our main. You don't need to modify this part.
Just run your file to make sure each function does
what it's supposed to do.

Uncomment the lines after you've written the required
function to make sure your code works properly.


"""   


if __name__ == "__main__":
    print("I am here")    
#    # call greet_print to greet michael
    greet_print("Michael")
#    
#    
#    
#    
#    # call greet_return to construct greeting for Jane
    greet_jane = greet_return("Jane")
#   
    print(greet_jane)
#    
#    
#    
#    
#    # call times5 to compute 10 * 5
    print("10 times 5 is ", times5(10))
#    
#    
#    
#    
#    # call isEven to check if 23 is an even number
    if isEven(23):
        print("23 is even.")
    else:
        print("23 is not even.")
#        
#    
#    
#    # call company_eps_5 to return the list of companies 
#    # whose eps >= 5
#    
    print("The companies whose eps >= 5 are: ", company_eps_5())
#    
#    
#    
#    # call reverseAnd10x_forloop to reverse my_list
#    
    my_list = [1, 2, 3, 4, 5, 6, 7]
#    
    print("Use a for-loop to reverse my_list and multiply by 10: ",
          reverseAnd10x_forloop(my_list))
#    
#    
#    
#    # call reverseAnd10x_listcomp to reverse my_list
#    
    print("Use list comprehension to reverse my_list and multiply by 10: ", 
          reverseAnd10x_listcomp(my_list))    
