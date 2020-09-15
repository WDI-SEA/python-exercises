# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]


# write function that takes a list and a number
def multiply_by(list, num):
  # loop through list items
  result = []
  for i in range(len(list)):
    # multiply each item by the list num
    # append to new array
    result.append(list[i] * num)
  # return multiplied array
  print(result)

multiply_by([5, 2, 15], 5)