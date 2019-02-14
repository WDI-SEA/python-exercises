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

# One-liner
from functools import reduce
from operator import mul
def factorialReduce(n):
    return reduce(mul, range(1, n + 1), 1)

for i in range(10):
    print(f"{i}!: {factorialReduce(i)}")


# Recursive iteration
# breaks at 997!
def factorialIter(n):
    def iter(acc, i):
        return acc if i > n else iter(i * acc, i + 1)
    return iter(1, 1)

for i in range(10):
    print(f"{i}!: {factorialIter(i)}")



# Pythonic?
from math import factorial

for i in range(10):
    print(f"{i}!: {factorial(i)}")