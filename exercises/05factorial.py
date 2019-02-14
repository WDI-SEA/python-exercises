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
	if isinstance(num, int):
		list = [num]
		i = num
		while i>1:
			list.append(i-1)
			i-=1
		k = 0
		result=num
		while k<num-1:
			result = result * list[k+1]
			k+=1
		print(result)
	else:
		print("Sorry, not an integer")
	

factorial(5)
