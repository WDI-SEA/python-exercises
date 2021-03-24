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

def factorial(num: int) -> int:
  # start the running total at 1 
  product = 1
  # loop in range of 1 to number + 1
  for i in range(1, num + 1):
    # set the product to be itself multiplied by i
    product *= i
  
  # return the product after looping
  return product

solution = factorial(5)

print(solution)