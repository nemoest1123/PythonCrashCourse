# Python Template for Geany

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print("It starts at the " + str(pi_string.index(birthday)) + "th digit")
    print("Here are the 6 numbers before and after your birthday: " +
        pi_string[pi_string.index(birthday)-6:pi_string.index(birthday)+12])
else:
    print("your birthday does not appear in the first million digits of pi!")
