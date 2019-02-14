# Write a method called `print_contacts` that takes a
# dictionary of key-value pairs for names and phone numbers,
# then outputs the `name` with the contact info.
#
# Try iterating over a dictionary with a for loop and printing
# out what values come back.
#
# Example method call:
#
# print_contacts(contacts)
#
# > Brian has a phone number of 333-333-3333
# > Lenny has a phone number of 444-444-4444
# > Daniel has a phone number of 777-777-7777
#
# Use the contacts below

contacts = {"Brian": "333-333-3333", "Lenny": "444-444-4444", "Daniel": "777-777-7777"}


def print_contacts(contacts):
    for (key, value) in contacts.items():
        print(f"{key} has phone number of {value}")


# Uh, you need Python 3.6 and above for f-strings. But it's worth it.
print_contacts(contacts)
