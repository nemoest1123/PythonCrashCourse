# Python Template for Geany

#~ pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#~ print(pets)

#~ while 'cat' in pets:
	#~ pets.remove('cat')

#~ print(pets)

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='rabbit', pet_name='richard')
describe_pet(pet_name='chuck', animal_type='plant')
