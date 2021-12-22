# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
text=input("alphabetize something: ")
letters=[]
def alphabetize(text):
    for i in text:
        letters.insert(0, i)
        letters.sort()
    print(("".join(letters)))
alphabetize(text)