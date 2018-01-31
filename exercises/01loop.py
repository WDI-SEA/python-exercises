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


def p_times(input_string, num_times=1):
    if num_times is None or num_times <= 0:
        print('None or 0')
        num_times = 1

    for i in range (0, num_times):
        print(input_string)


# Call the function
p_times('hi')
