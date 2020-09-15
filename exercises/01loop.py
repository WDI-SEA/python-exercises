# Write a method called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example method call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there


statement = input("Type a statement: ")
num = int(input("Now type a number of times you'd like me to repeat this statement: "))

for i in range(num):
    print(statement)
