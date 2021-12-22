# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def method_type():
    method = input("What calculation would you like to do? (add, sub, mult, div): ")
    if method == "add":
        num1 = input("what is number 1: ")
        num2 = input("what is number 2: ")
        print(f"your output is: {int(num1) + int(num2)}")
    elif method == "sub":
        num1 = input("what is number 1: ")
        num2 = input("what is number 2: ")
        print(f"your output is: {int(num1) - int(num2)}")
    elif method == "mult":
        num1 = input("what is number 1: ")
        num2 = input("what is number 2: ")
        print(f"your output is: {int(num1) * int(num2)}")
    elif method == "div":
        num1 = input("what is number 1: ")
        num2 = input("what is number 2: ")
        print(f"your output is: {int(num1) / int(num2)}")
method_type()