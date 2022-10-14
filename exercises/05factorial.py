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
    # keep tract of factorial
    # prod = 1
    # # loop up to the num and multiply the product by each number
    # for i in range(1, num + 1):
    #     prod *= i
    # i = 1
    # while i < num + 1:
    #     prod *= i
    #     i += 1

    # base case -- stopping the recursive loop
    if num < 3:
        return num
    
    # recursive case
    return num * factorial(num - 1)

print(factorial(5))