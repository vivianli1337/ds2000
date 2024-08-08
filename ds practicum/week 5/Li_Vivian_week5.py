### Company Directory

# Create a list of company_names,
# CEOs, EPS_2018 (annual diluted earnings per share)

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



### Helper functions:

def percent_vowels(text):
    """ 
    This function takes a text (string) as input and computes the percentage
    of vowels (aeiou) in the string


    name: percent_vowels
    input: text (string) (without punctuations)
    output: percentage (float)
    """
    count=0
    for i in text:
        if i in "aeiouAEIOU":
            count+=1
    return count/len(text)

"""


!!! Helpful techniques:

# For loop iteration by position:
>>> mylist=[1,30,29]
>>> for i in range(len(mylist)):
	print(i, "--", mylist[i])

0  --  1
1  --  30
2  --  29

# For loop iteration by value:

>>> for i in ["hi","mango","cat"]:
........print(i)

hi
mango
cat


>>> "hi" in ["hello", "hey", "hi"]
True



# Check if a string contains a specific letter:

>>> myletter='a'
>>> mystring='apple'
>>> myletter in mystring
True


# Split a string into different parts based on separator
# the result will be a list of separated elements.
>>> "hey-you".split('-')
['hey', 'you']

# Access elements of a nested list

>>> list1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> list1[0]
[1, 2, 3]
>>> list1[0][1]
2

# List comprehension 

>>> [i*2 for i in [1,2,3]]
[2, 4, 6]

"""
def main():
    """
    Q1:

        Create a list named companies_2018
        Then write a for loop to append the company names from DATA
        to companies_2018.
        
        Print the completed list.
    
    """
    companies_2018 = []
    for i in DATA:
        companies_2018.append(i[0])
    print(companies_2018)


    """
    Q2:

        Create a list named company_EPS
        Then write a for loop to append the company EPS's from DATA
        to company_EPS.
        
        Print the completed list.
    
    """
    company_EPS = []
    for i in DATA:
        company_EPS.append(i[2])
    print(company_EPS)
    
    
    """
    Q3:
        Create a list named ceo_list
        Then write a for loop to append the CEO names from DATA
        to ceo_list. Make sure each name follows the "lastname, firstname" format
               
        Print the completed list
    
        Hint: You might want to use the split() function to split a string
    
    """
    ceo_list =[]
    for i in DATA:
        name = i[1]
        name = name.split(" ")
        ceo_list.append(name[1]+", "+name[0])
    
    print(ceo_list)
    
    """
    prof:
        ceo_list =[]
        for i in DATA:
            name = i[1]
            lastname = name.split(" ")[1] - using space as a separator
            firstname = name.split(" ")[0]
            finalname = lastname+','+firstname
            ceo_list.append(finalname)
        print(ceo_list)
    
    
    """
 

    """
    Q4:
        Apply the vowel percentage computation function (defined above as
        'percent_vowels') to the elements in the list of CEOs last names,
        and print each CEO's last name vowel percentage
        (e.g., Tim Cook has 50% vowels in his last name)
        
        Hint: You should experiment with the percent_vowels function to see
        what it does.
        
        
    """
    ceo_last =[]
    for i in DATA:
        last = i[1]
        last = last.split()
        ceo_last.append(last[1])
    
    value =[]    
    for i in ceo_last:
        vowels = percent_vowels(i) 
        value.append(vowels)
        

    print(value)
    
    
    """
    professor's:
        vowel_list =[]
        for ceo in ceo_list:
            lastname = ceo.split(",")[0]
            vowel_list.append(percent_vowels(lastname))
        print(vowel_list)
    """

    """   
    Q5:
        
        Create a list called company_eps_5.
        
        Specify a loop that appends the first 3 letters (uppercase) of the name
        of companies whose EPS is >=5.0. These values should be appended
        to company_eps_5.
        
        Print the completed list
    
        Hint 1: You can iterate over a string as if it is a list of letters
        Hint 2: You can use the upper() function to convert letters to uppercase
    
    """

    company_eps_5 = []
    for i in DATA:
        EPS = i[2]
        companyname = i[0]
        companyname = companyname[:3]
        companyname = companyname.upper()
        
        if EPS >= 5.0:
            company_eps_5.append(companyname)
    
    print(company_eps_5)
    
    """
    professor's:
        company_eps_5 =[]
        for company in DATA:
            if company[2]>=5:
                company_eps_5.append(company[0][:3].upper)
    """

    
    """
    Q6:
        Create an empty list called my_numbers.
        
        Write a for loop to append the following numbers to my_numbers:
            3, 6, 9, ..., 87, 90
            
        Print my_numbers.
        
        Hint: use the range() function to produce a sequence of integers
            
        we stopped at #5; below are my attempted tries
    """
    my_numbers = []
    
    for i in range(3,91):
        my_numbers.append(i)
     
    
    print(my_numbers[:91:3])




    """
    Q7:
        Use list comprehension to create a list called my_numbers_2 that
        contains the following numbers:
            3, 6, 9, ..., 87, 90
            
        Print my_numbers_2.
            
    """
    my_numbers_2 = []
    
    for i in range(3,91):
        my_numbers_2.append(i)
    
    print(my_numbers_2[:91:3])




    """
    Q8:
        Define my_list to contain numbers 1, 2, ..., 20
        Write a for loop to multiply all even numbers by -1
        
        Print the modified my_list
    """
    my_list = []
    
    for i in range(1,21):
        my_list.append(i)
        list = my_list[1:21:2]
        """
        not sure how to multiple a list with -1
        new_list = -1 * list (?)
        """
         
        
    print(list)
        
        
        


    
main()
