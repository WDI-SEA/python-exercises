# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(li, num):
    # iterate the list in a way that allows us to mutate the list
    # for i, list_num in enumerate(li):
    #     li[i] = list_num * num
    
    # for i in range(len(li)):
    #     li[i] *= num
    # list comprehension -- returns a new list
    # [return expression for varaible in iterable (if expression)]
    return [list_num * num for list_num in li]

print(multiply_by([1, 2, 3], 5))