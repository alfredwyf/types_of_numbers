def isTriangular(x):
    """Returns whether or not a given number x is triangular.
    
    The triangular number Tn is a number that can be represented in the form of a triangular 
    grid of points where the first row contains a single element and each subsequent row contains 
    one more element than the previous one.
    
    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.
    
    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)
    
    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """
    if num == 1:
        return True
    
    NumFact = []
    Check = []
    
    for k in range(1, x + 1):
        NumFact.append(k)    
    
    for j in NumFact:
        if x == (j * (j + 1)) / 2:
            Check.append(j)
    
    if len(Check) >= 1: #check if any number is stored in the list of Check to identify if the result of Triangular is ture or not
        return True
    else:
        return False

    
#Reading number    
num = input("please input an intger:")
num = int(num)
print(isTriangular(num))  

if isTriangular(num) == True:
    print(int(num), "is a Triangular number")
else:
    print(int(num), "is not a Triangular number")