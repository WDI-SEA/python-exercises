# Question 1, Loop

def p_times():
    user_statement = input("Enter a statement: ")
    number = int(input("Enter how many times: "))
    for _i in range(1, number + 1):
        print(user_statement)

p_times()

# Question 2, Letter Count

dd = {}

def letter_count(string):
    global dd

    for letter in string:
        if letter not in dd:
            dd[letter] = 1
        elif letter in dd:
            dd[letter] +=1
    return dd

print(letter_count("Hello"))

# Question 3, Print Contacts

contacts = {
  'Brian': '333-333-3333',
  'Lenny': '444-444-4444',
  'Daniel': '777-777-7777'
}

def print_contacts(phonebook):
    for contact in phonebook:
        if contact in phonebook:
            value = phonebook[contact]
            print(f"{contact} has a phone number of {value}")
        

print_contacts(contacts)

#Question 4, Multiply By

my_array = [2, 14, 3]

def multiply_by(array, num):
    print(list(map(lambda x: x * num, array)))

multiply_by(my_array, 2)

# Question 5, Factorial

def factory(n):
    new_num = 1
    for digit in range(1, n + 1):
        new_num *= digit
    return new_num

print(factory(5))