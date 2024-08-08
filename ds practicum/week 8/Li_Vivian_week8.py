### Week 8 Exercise
### Make sure the file "starbucks_menu.csv" is saved in the same folder
### as this script





import csv






### Some basic information about coffee shops nearby


shops = ["Starbucks", "Tatte", "Dunkin", "Pavement"]
locations = ["Curry", "Marino", "Huntington", "Huntington"]
ratings = [3.6, 4.4, 3.6, 4.3]
numbers = ["(617)373-2530", "(617)263-8989", "(617)373-4611", "(617)859-7080"]







def CreateCoffeeDict():
    """
    Load the 4 coffee related lists defined above, and create a list of dicts
    where each dict has the following format:

    {shop: "Starbucks", location: "Curry", rating: 3.6, number: "(617)373-2530"}


    return: coffee_list (a list of dicts)
    """
    places = []
    
    for i in range(0, len(shops)):
        coffee_place = {}
        coffee_place["shop"] = shops[i]
        coffee_place["location"] = locations[i]
        coffee_place["rating"] = ratings[i]
        coffee_place["number"] = numbers[i]
        
        places.append(coffee_place)
   
    return places


### In this function, make sure to return a list, where the first
### element of the list is the header list, and the second is the
### rest of the data in the form of a list of lists.
### In other words, your code should separate the header
### row from the rest of the data
###
### You need to use "with open(filename, encoding = "utf8") as csv_file" to
### read in the data.


def read_starbucks_data(filename):
    ''' Function read_starbucks_data

        name: read_starbucks_data
        input: filename (string)
        returns: list [header, menu]
                 header is a list
                 menu is list of lists
    '''


    starbucks_data=[]
    with open(filename, encoding="utf8") as infile:
        csv_file = csv.reader(infile, delimiter=',')
        for row in csv_file:

            starbucks_data.append(row)

        #starbucks_data ### complete list including headers
        header = starbucks_data[0]
        menu = starbucks_data[1:]

    return [header, menu]


### In the function below, use the header to determine
### which column contains beverage_category
###
### Hint: you can use the list.index() method to determine the index of a given element

def retrieve_smoothies(header, menu):
    """ This function returns a list of just smoothie products

    name: retrieve_smoothies
    input: header (list) menu (list of lists)
    output: smoothie_list (list of lists containing just smoothies)

    """
    # stopped here: incomplete
    #smoothie_list = []
    
    #pos = menu.index("Smoothie")
    #for category in menu:
    #    if menu[pos] not in smoothie_list:
    #       smoothie_list.append(menu(pos))
    
    #return smoothie_list

            




### In the function below, use the header to determine
### which column contains Beverage_category and which column
### contains Calories
###
### Hint: you can use the list.index() method to determine the index of a given element

def get_category_calories_average(category_name, header, menu):
    """ Given a beverage category, this function returns the
    average calories of all beverages in that category

    name: get_category_calories_average
    input: category_name (string)
           header (list)
           menu (list of lists)
    output: average_calories (float)

    """







def main():
    
    
    ### First, load coffee shop information
    
    
    ### Q1: Write the CreateCoffeeDict function
    print("\nQ1:")
    shop_list=CreateCoffeeDict()
    print(shop_list)
    
    
    
    ### Q2. Write a loop to print all shop-location combinations using the
    ### list of dicts created through calling CreateCoffeeDict()
    ### Each shop-location string should be printed using the following format:
    ### "Starbucks -> Curry", "Tatte -> Marino", etc.

    print("\nQ2:")
   
    for i in shop_list:
        name = i["shop"]
        location = i["location"]
        print(name, "-->", location)



    ### Q3. Iterate over the Tatte dictionary and print the key names.
    ### Again, you should use the shop_list created above. Specifically,
    ### you can use shop_list[1] to refer to the Tatte dictionary

    print("\nQ3:")        
    
    for elements in shop_list[1]:
        print(elements)
    


    ### Q4. Iterate over the Dunkin dictionary and print the values
    print("\nQ4:")
    
    for elements in shop_list[2].values():
        print(elements)


    ### Q5. Iterate over the Pavement dictionary and print each "key: value"
    ### combination as a string. E.g. "Shop: Pavement"
    ###
    ### Hint: you can use dict.items() to iterate over each key-value combination.
    ### When iterating over a dict using .items(), each item is a 'tuple'
    ###
    ### Tuple is a special type of list: you can't change the elements of a tuple
    ### once they are defined. (I.e., they are immutable). 
    ### 
    ### 
    ### To create a tuple, use parentheses.
    ###     E.g., my_tuple = (2, 3)
    ###
    ### You can access different elements of a tuple using index just like lists.
    ###     E.g. my_tuple[0] returns the first element of my_tuple.
    
    print("\nQ5:")    

    for elements in shop_list[3].items():
        print(elements[0] + ": " + str(elements[1]))
        
 
    
    ### WE STOPPED HERE ###
    ### Questions below use the Starbucks data
    ### Note: I've written the read_starbucks_data function above, so the
    ### following 2 lines already load the data for you. Scroll down and
    ### answer Q6 and Q7.
    
       
    [header, starbucks] = read_starbucks_data("starbucks_menu.csv")
    print("\nThe original header row is ", header)




    ### Q6: Complete the function "retrieve_smoothies
    print("\nQ6:")
    print("The number of smoothies on the menu is ",
          len(retrieve_smoothies(header, starbucks)))



    ### Q7: Complete the function "get_category_calories_average"    
    print("\nQ7:")
    print("The average calories of the Coffee category is ",
          get_category_calories_average("Coffee",header, starbucks))




main()
