# Python Template for Geany

import pizza

toppings = []
topping = ''

while topping != 'go':
        
    topping = input("Enter a topping or 'go' to make the pizza: ")
    
    if topping != 'go':
        toppings.append(topping)
    else:
        pizza_size = input("How big (inches): ")
        pizza.make_pizza(pizza_size, toppings)
