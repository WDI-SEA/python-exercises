# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    print(f"this is printing i - {i}")
    result = result * int(i)
    print(f"this is printing result - {result}")




# Example method call
#
factorial(5)
#
# > 120
#
