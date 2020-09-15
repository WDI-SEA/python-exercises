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

def factorial(num):
    temp = num
    for i in range(1, num):
        temp1 = (num - i)
        temp = temp * temp1 # 5 * 4 * 
    return temp

print(factorial(5))