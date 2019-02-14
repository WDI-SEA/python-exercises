# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
def factorial(number):
  multiply = 1
  for num in range(number):
    multiply = (num + 1) * multiply
  print(multiply)

# Example method call
#
factorial(5)
#
# > 120
#
