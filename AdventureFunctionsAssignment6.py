# Timothy Fox
# 2/24/2025

# This is the Adventure Functions project. It lays out a 
# few basic functions (purchase_item and new_random_monster)
# to be used in an adventure game
#----------------------------------------------------------------------------

# Timothy Fox
# 3/1/2025
# Assignment 6
# Added welcome function
# Added shop menu function 


import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase = 1):

#Logic for finding how many of an item the player can afford

    if itemPrice * quantityToPurchase < startingMoney: 
        pass
    elif itemPrice * quantityToPurchase > startingMoney:
        while itemPrice * quantityToPurchase > startingMoney and quantityToPurchase > 0:
            quantityToPurchase -= 1
        pass


#Transaction logic

    quantityPurchased = quantityToPurchase
    remainingMoney = startingMoney - itemPrice * quantityToPurchase 
    print(f'Purchased {quantityToPurchase} (item name filler)(s)')
    print(f'${remainingMoney} Money remaining')

# --TO DO-- code for giving player purchased items and updating global money goes here

    return remainingMoney, quantityPurchased
    # I didn't know how to set up a function for returning without knowing what the 
    # rest of the code would look like so I just printed for now     

def new_random_monster():
    
    #This is the list of monsters and their traits
    
    monster_dict = [
        {
        'name': 'Slime',
        'desc': 'A small clump of rotting biomatter clung together by the collective, dying will of its parts',
        'health': (1, 3),
        'power': (0, 2),
        'money': (5, 10)
    },
    {
        'name': 'Zombie',
        'desc': 'Any dead creature with enough soul left to continue to move',
        'health': (20, 50),
        'power': (10, 20),
        'money': (20, 60)
    },
    {
        'name': 'Greg',
        'desc': 'Greg is a wealthy passerby. Will you sacrifice your morality for wealth?',
        'health': (8, 12),
        'power': (1, 3),
        'money': (2000, 5000)
    }
    ]

    #This is the logic for creating a new monster using random

    monster = random.choice(monster_dict)
    return {
        'name': monster['name'],
        'desc': monster['desc'],
        'health': random.randint(*monster["health"]),
        'power': random.randint(*monster['power']),
        'money': random.randint(*monster['money'])
    }


#--------------------------------------------------------------------------------------------------------------------------------
# New functions for assignment 6 below line

def print_welcome(name, width=20):

#pretty straight forward, just prints the welcome

    print(f'{"Hello, " + name + "!":^{width}}')

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):

#    Prints the formatted shop
    
    
#    item1Name: name of item 1
#    item1Price: price of item 1
#    item2Name: name of item2
#    item2Price: price of item 2
    
#   --To Do-- Add returns instead of just printing when the game has more structure and the values can be returned somewhere.

    print("/---------------------\\")
    print(f'| {item1Name:<12} ${item1Price:6.2f} |')
    print(f'| {item2Name:<12} ${item2Price:6.2f} |')
    print("\\---------------------/")

# these are function calls to showcase functionality
print('This test shows what happens when the player does not have enough money to purchase an item\n')
purchase_item(100, 50, 1)
print('\n\n')
print('This is what happens when a player requests more items than they can afford but can still afford some\n')
purchase_item(10, 30, 5)
print('\n\n')
print('This is what happens when a player purchases items correctly\n')
purchase_item(10, 100, 4)
print('\n\n')

print('This is just showcasing the new_random_monster function\n')
monster = new_random_monster()
print(monster, '\n\n')
monster = new_random_monster()
print(monster, '\n\n')
monster = new_random_monster()
print(monster, '\n\n')

# Functions for assignment 6 to showcase functionality

print('\n\nWelcome message tests\n\n')
print_welcome('Jeff')
print_welcome('Tom')
print_welcome('NoobSlayer3000')

print('\n\nShop menu tests\n\n')
print_shop_menu("Bow", 125.75, "Arrow", 2.50)
print_shop_menu("Potion", 10.50, "Wand", 299.99)
print_shop_menu("Sword", 135.80, "Shield", 99.99)
