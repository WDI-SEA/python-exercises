# Write a method called `multiply_by` that takes a number and
# array, and returns the array of numbers multiplied by that number.
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

def multiply_by(list, num):
	result = []
	i=0
	while i<len(list):
		product = list[i] * num
		result.append(product)
		i+=1
	print(result)

multiply_by([1,2,3,4], 5)
