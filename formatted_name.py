# Python Template for Geany

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
#~ musician = get_formatted_name('jimi', 'hendrix')
#~ print(musician)

#~ musician = get_formatted_name('john', 'hooker', 'lee')
#~ print(musician)

while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    #this isn't complete
