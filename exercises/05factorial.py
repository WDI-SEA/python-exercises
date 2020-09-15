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

def factorial(number):
  result = 0
  for n in range(1, number + 1):
    if (result == 0):
      result = n
    else:
      result *= n
  return result

print(factorial(6))
