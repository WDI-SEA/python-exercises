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


print(range(1, 10))

def factorial(num):
    
    if num < 3:
        return num
    
    return num * factorial(num - 1)

    return prod

print(factorial(5))