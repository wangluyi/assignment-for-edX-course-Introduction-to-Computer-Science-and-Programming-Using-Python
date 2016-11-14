# -*- coding: cp936 -*-
def ndigits(x):
    '''a function called “ndigits”,
   that takes an integer ‘x’ (either positive or negative) as an argument.
   This function returns the number of digits in the integer x.
    '''
    
    #deal with the integer smaller than 0
    if x<0:
        x=0-x
        
    #use recursion to do the work
    if x<10:
        return 1
    else:
        return ndigits(x/10) + 1

