def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """
    
    Composite = []
    
    for i in range(1, x + 1):
        if (x % i == 0):
            Composite.append(i)
        
    if len(Composite) > 2:
        Composite = True
        print(num, "is a Composite number")
    else:
        Composite = False
        print(num, "is not a Composite number")
        
    return Composite   

#Reading number
num = input("please input an intger:")
num = int(num)
print(isComposite(num))