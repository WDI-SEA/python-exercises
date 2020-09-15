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


def p_times(num, statement):
    for i in range(num):
        print(statement)


p_times(7, "Boots and Cats and")
p_times(4, "THANKS PETE")
p_times(2, "Let's GOOOOOOOOOOO")
