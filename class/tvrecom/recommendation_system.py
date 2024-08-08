
#driver
from review import Review
# review = module

LANEY_SHOWS = [{"Name" : "Laney", "Show Title" : "The West Wing", "Platform" : 
                "HBO Max", "Rating" : 5, "Times Watched" : 20},
               {"Name" : "Laney", "Show Title" : "Buffy", "Platform" :
                "Amazon Prime", "Rating" : 5, "Times Watched" : 3},
               {"Name" : "Laney", "Show Title" : "Pitch", "Platform" :
                 "Hulu", "Rating" : 4, "Times Watched" : 1}, 
                {"Name" : "Laney", "Show Title" : "Brooklyn 99", "Platform" :
                 "Hulu", "Rating" : 4, "Times Watched" : 4}, 
                {"Name" : "Laney", "Show Title" : "The Great British Bake Off",
                 "Platform" : "Netflix", "Rating" : 5, "Times Watched" : 1},
                {"Name" : "Laney", "Show Title" : "Friends", "Platform" :
                 "HBO Max", "Rating" : 4, "Times Watched" : 1},
                    {"Name" : "Laney", "Show Title" : "Gilmore Girls", "Platform" :
                 "Netflix", "Rating" : 5, "Times Watched" : 7}]

def make_laney_objs(list_of_dict):
    ''' Function: make_laney_objs
        Parameter: list of dictionaries wheere one dictionary = one show
        Returns: list of Review objects
    '''
    reviews = []
    for item in list_of_dict:
        name = item["Name"]
        title = item["Show Title"]
        rating = item["Rating"]
        review = Review(name, title, rating)
        reviews.append(review)
    return reviews
    
def make_prompt_objs(friend):
    ''' Function: make_prompt_objs
        Parameters: friend's name (string)
        Returns: list of objects, created by prompt the user for info
    '''
    reviews = []
    for i in range(3):
        title = input("Enter name of show\n")
        rating = int(input("What's your rating of it?\n"))
        review = Review(friend, title, rating)
        reviews.append(review)
    return reviews

def make_recommendation(laney_review, friend_reviews):
    ''' Function: make_recomkmendation
        Parameters: list of Reivew objs (Laney), list of review objs (recommender)
        Returns: list of review objs (recommended shows)
    '''
    recs = []
    for review in friend_reviews:
        if review.rating > 3 and review not in laney_review:
            recs.append(review)
    return recs
    

def main():
    # step 1 gather data from Laney and Friend
    # make a list of review objects for laney
    laney_reviews = make_laney_objs(LANEY_SHOWS)
    friend = input("Who is making recommendations?\n")
    friend_reviews = make_prompt_objs(friend)
    
    # Print out object so far
    print("Laney's shows so far...")
    for review in laney_reviews:
        print(review)
    print("\n")
       
    # Call the recommender function
    recs = make_recommendation(laney_reviews, friend_reviews)
   
    # Step three --- communicate! Print out recommendations
    print(friend, "thinks you should watch...")
    for show in recs:
        print(show)
   
main()