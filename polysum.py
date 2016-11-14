import math
def polysum(n,s):
    '''
    this is to calculate the sum of 
    the area and square of the perimeter of the regular polygon
    '''
    area=0.25*n*(s**2)/math.tan(math.pi/n)
    perimeter=n*s
    ans=area+(perimeter)**2    #ans is the sum
    return round(ans,4)