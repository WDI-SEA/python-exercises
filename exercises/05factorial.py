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
  if n is None or type(n) is not int or n < 0:
    print('Invalid value for n')
    return -1

  total = 1
  for i in range(1, n+1):
    total *= i

  print(total)


# Call the function
factorial(5)
