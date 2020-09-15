# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the list.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(list, number):
   new_list = []
   for num in list:
        # print(item)
       new_list.append(num * number)
   return new_list

print(multiply_by([1,2,3], 5))
print(multiply_by([2,4,6], 10))
print(multiply_by([3,6,9], 15))