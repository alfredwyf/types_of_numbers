def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """
    
    Abundant = []
    
    for i in range(1, x + 1):
        if (x % i == 0):
            Abundant.append(i)

    Abundant.pop() #remove the last number from the list
        
    if x < sum(Abundant): #sum up all numbers/elements from the list and compare it with num and see if the sum is larger
        print(x, "is an abundant number, since the sum of its factor(s) is greater than", x)
        Abundant = True
    else:
        print(x, "is not an abundant number, since the sum of its factor(s) is smaller than", x) 
        Abundant = False
        
    return Abundant

#Reading number
num = input("please input an intger:")
num = int(num)
print(isAbundant(num))