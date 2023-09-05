# Ask user for their name
name = input("What is your name ? ").strip().title()

# Remove whitespace from str and captalize user's name
# name = name.strip().title()

#Capitalize user's name
# name = capitalize()

# split user's name into  first name and last name
first, last = name.split(" ")

# say hello to user
# print (f" hello, {name}")
print (f" hello, {last}")