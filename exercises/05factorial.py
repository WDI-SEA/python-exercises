# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#

def factorial(num):
    # a running total of the factorial
    product = 1
    # loop up to num (including num) and multiply by procdut
    for i in range(1, num + 1):
        product *= i
    
    return product
    hello = 10

print(factorial(5))