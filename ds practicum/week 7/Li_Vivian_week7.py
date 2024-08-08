### Week 7 Exercise
### Make sure the file "starbucks_menu.csv" is saved in the same folder
### as this script





import csv



### In this function, make sure to return a list, where the first
### element of the list is the header list, and the second is the
### rest of the data in the form of a list of lists.
### In other words, your code should separate the header
### row from the rest of the data
###
### Hint:
###    You need to use "with open(filename, encoding = "utf8") as csv_file" to
###    read in the file.


def read_starbucks_data(filename):
    ''' Function read_starbucks_data

        name: read_starbucks_data
        input: filename (string)
        returns: list [header, menu]
                 header is a list containing the header row
                 menu is list of lists containing the remaining rows
    '''
    starbucks_data = []
    
    with open(filename, encoding="utf8") as infile:
        csv_file = csv.reader(infile, delimiter = ",")
        for row in csv_file:
            starbucks_data.append (row)
           
            header = starbucks_data[0]
            menu = starbucks_data[1:]
    return [header, menu]
            

def add_itemid(header, menu):
    """ Function to add a column of item IDs to the header and menu.
    The first product on the menu should be Item 0, the second product on the 
    menu should be Item 1. Make sure the ItemID column is inserted at the
    beginning of each list.
    
    Hint: You can use the "insert" function to insert an element to a specified
          position in the list. Syntax: your_list.insert(index, item_to_insert)


    name: add_itemid
    input: header (list), menu (list of lists)
    output: none (void)

    """
    header.insert(0, "Item ID")
    for item_index in range(len(menu)):
        menu[item_index].insert(0, item_index)
        
""" 
    or 
    row_number = 0
    in row in menu:
        row.insert(0, row_number)
        row_number += 1
"""


### In the function below, use the header to determine
### which column contains beverage_category
def count_beverage_category(header, menu):
    """ This function detects the Beverage_category column.
    Then it counts the number of beverage categories
    
    Hint 1: You can use the "index" function to locate the index of a given
            element.
    Hint 2: You can use the following syntax to check whether a given element
            is in the list:
                
            an_element in a_list
            
            Similarly, you can check whether a given element is NOT in the list:
            
            an_element not in a_list

    name: count_beverage_category
    input: header (list), menu (list of lists)

    output: number of distinct categories (int)
    """
    
    beverage_category = []
    
    pos = header.index("beverage_category")
    for order in menu:
        if order[pos] not in beverage_category:
           beverage_category.append(order(pos))
    
    return len(beverage_category)

    
    
#####  we stopped here in class -----------
### In the function below, use the header to determine
### which column contains beverage_category
def retrieve_smoothies(header, menu):
    """ This function returns a list of just smoothie products

    name: retrieve_smoothies
    input: header (list) menu (list of lists)
    output: smoothie_list (list of lists containing just smoothies)

    """
 














### In the function below, use the header to determine
### which column contains Beverage_category and which column
### contains Calories
def get_category_calories_average(category_name, header, menu):
    """ Given a beverage category, this function returns the
    average calories of all beverages in that category

    name: get_category_calories_average
    input: category_name (string)
           header (list)
           menu (list of lists)
    output: average_calories (float)

    """
    













### Optional challenge question
###
### In the function below, use the header to determine
### which column contains Beverage_prep
def get_beverage_size(header, menu):
    """ This function should do the following:
    1. create a new column in the header named "Size"
        This new column should be appended at the end of header

    2. for each item, use the "Beverage_prep" column to determine
        the correct size of the item, and append the size to the
        end of the list for this item

    3. check the csv file (e.g., open it in Excel) and identify the
        logic to determine the size of each beverage

    
    Hint: There are 4 sizes (Short, Tall, Grande, Venti)
    
    name: get_beverage_size
    input: header (list)
           menu (list of lists)

    output: header (list, updated header)
            menu    (list of lists, updated menu)

    """






def main():
    
    [header, starbucks] = read_starbucks_data("starbucks_menu.csv")

    print("The original header row is ", header)
    print(starbucks)


    print("\nNow add an ID column (ItemID)...")
    add_itemid(header, starbucks)
    

    num_types = count_beverage_category(header, starbucks)
    print("\nThere are ", num_types, " different categories.")

    
    print("\nThe average calories of the Coffee category is ",
          get_category_calories_average("Coffee",header, starbucks))



    print("\nThe number of smoothies on the menu is ",
          len(retrieve_smoothies(header, starbucks)))


    ### The lines below are for the optional challenge question
    
    print("\nNow adding a new column (size) to the data...")

    updated_header, updated_menu = get_beverage_size(header, starbucks)
   

    print("\nThe updated header row is ", updated_header)
    print("\nAs an example, the list for item 5 (Latte with 2% milk) is ",
          updated_menu[5])



main()
