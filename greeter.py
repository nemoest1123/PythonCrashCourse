# Python Template for Geany

def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'jesse']
greet_user(usernames)
