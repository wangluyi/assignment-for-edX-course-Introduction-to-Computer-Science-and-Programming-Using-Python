def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    
    d_intersect = {}
    d_difference = {}
    
    for key in d1:
        if d2.has_key(key):
            d_intersect[key] = f(d1[key] , d2[key])
        else:
            d_difference[key] = d1[key]
    
    for key in d2:
        if d1.has_key(key)==False:
            d_difference[key] = d2[key]
            
    return (d_intersect,d_difference)