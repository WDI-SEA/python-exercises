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
  factorial_result = 0
  for number in range(1, n + 1):
    if (factorial_result == 0):
      factorial_result = number
    else:
      factorial_result *= number
  return factorial_result

print(factorial(5))
