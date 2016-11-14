def nfruits(dict, fruits_eaten):
    '''
    a function "nfruits" that takes two arguments:

* A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home (length < 10)
* A string pattern of the fruits eaten by Python on his journey as observed by Cobra.

This function should return the maximum quantity out of the different types of fruits that is available with Python when he has reached the campus.
    '''
        
    for item in fruits_eaten[:-1]:
        for fruit in dict:
            if fruit==item:
                dict[fruit] -= 1
            else:
                dict[fruit] += 1
                
    #deal with the last eaten fruit
    item = fruits_eaten[-1]
    for fruit in dict:
        if fruit==item:
            dict[fruit] -= 1

    #find the maximum of quantity of the fruits left
    max_fruit = 0
    for fruit in dict:
        if dict[fruit] > max_fruit:
            max_fruit = dict[fruit]
    return max_fruit