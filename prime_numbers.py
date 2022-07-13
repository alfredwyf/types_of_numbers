def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    Prime = []

    for i in range(1, x + 1): 
        if (x % i == 0):
            Prime.append(i)

    if len(Prime) == 2:
        Prime = True
        print(num, "is a Prime number")
    else:
        Prime = False
        print(num, "is not a Prime number")

    return Prime

#Reading number
num = input("please input an intger:")
num = int(num)
print(isPrime(num))