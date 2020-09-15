# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#
def factorial(n):
    numb1 = 1
    while ( n>=1 ):
        numb1 = numb1 * n
        print(n)
        n= n-1
    print(numb1)

factorial(5)
