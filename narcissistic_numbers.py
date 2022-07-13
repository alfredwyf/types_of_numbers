def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """
    global num
    num = str(num)
    Numlen = len(num)
    sum = 0
    for i in num:
        sum += int(i) ** Numlen
    return sum == int(num)


#Reading number
num = int(input("please input an intger:"))
print(isNarcissistic(num))  

if isNarcissistic(num) == True:
    print(int(num), "is a Narcissistic number")
else:
    print(int(num), "is not a Narcissistic number")