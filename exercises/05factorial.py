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
  result = 0
  # invoke reversed() to reverse the range (fun and new!)
  for i in reversed(range(1, num + 1)):
    # account for fencepost of first num and add it directly to result
    if (i == num):
      result += num
    # if it is not the first number, multiply the result by i
    else:
      result *= i
  print(result)


factorial(10)