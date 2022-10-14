# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 2}

def letter_count(string):
    dd = {}
    # loop over string
    for taco in string:
        # if the taco is in our dict, we want to increment that value
        if taco in dd:
            dd[taco] += 1
        # if the taco is not in our dict we want to add it to the dict 
        # with a value of 1
        else:
            dd[taco] = 1
    
    return dd

string = 'taco'

for char in string:
    print(char)

for i in range(len(string)):
    print(string[i])

for i, char in enumerate(string):
    print(i, char)

print(letter_count('banana'))
