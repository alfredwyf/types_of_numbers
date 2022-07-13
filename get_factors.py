def getFactors(x):
    """Returns a list of factors of the given number x.
    Basically, finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return
    """
    factors = []
    
    for i in range(1, x + 1):
        if (x % i == 0):
            factors.append(i)
        
    return factors

#Reading number
num = input("please input an intger:")
num = int(num)
print(getFactors(num))