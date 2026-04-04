class NegativeDimensionError(Exception):
    pass

def area(length,breadth):
    if length>=0 and breadth>=0:
        return length * breadth
    else:
        raise NegativeDimensionError('Please enter the length and breadth in positive numbers')
        
try:
    result = area(-5,3)
    print(result)
except NegativeDimensionError as e:
    print('Error : ',e)