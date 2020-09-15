# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.


my_list = [1, 2, 3, 4, 5]
my_new_list = []
my_int = 5
for i in my_list:
    my_new_list.append(i * my_int)

print(my_new_list)