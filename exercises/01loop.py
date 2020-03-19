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

# SOLUTION 1:

def p_times(statement, num):
    statement = statement + "\n"
    print(statement * num)

# SOLUTION 2:
def p_times(statement, num):
    i = 0
    while i < num:
        print(statement)
        i += 1

# SOLUTION 3:
def p_times(statement, num):
    for i in range(num):
        print(statement)
