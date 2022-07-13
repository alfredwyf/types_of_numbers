def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    
    Perfect = []
    
    for i in range(1, x + 1):
        if (x % i == 0):
            Perfect.append(i)

    Perfect.pop() #remove the last number from the list
        
    if x == sum(Perfect): #sum up all numbers/elements from the list and compare it with num and see if they are equal
        print(x, "is a perfect number, since the sum of its factor(s) is equal to", x) 
        Perfect = True
    else:
        print(x, "is a not perfect number, since the sum of its factor(s) is not equal to", x) 
        Perfect = False
        
    return Perfect   

#Reading number
num = input("please input an intger:")
num = int(num)
print(isPerfect(num))