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

# when you loop through a range, you are looping through every number 0 and up 
# when you want to loop through a list, you have to name the list instead of range


def multiply_by(arr, num):
    newList = []

    for i in arr:   
        newList.append(i * num) 
    print(newList)

multiply_by([1,2,3,4], 5)

