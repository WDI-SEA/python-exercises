# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
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

def p_times(statement, num):
    for _ in range(num):
        print(statement)

# range(start num = 0, end num, step = 1)

# one arg range(0, your arg here, 1)
# two args is range(your first arg, your second arg, 1)
# three args is range(arg one, arg 2, arg 3)
for i in range(0, 10, 2):
    print(i)

# # p_times('Hello there', 1)

# p_times('Hello there', 3)