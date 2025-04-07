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

#-------------------------------------------------------------------------------
# Timothy Fox
#3/7/2025
# assignment 8
# Changed this file from the main file to gamefunctions 

'''
These are the game functions. This module contains the funcitons necessary for the adventure game such as:
print_welcome
print_shop_menu
purchase_item
new_random_monster
'''
import json
import random



def save(inventory, HP, Gold, Name):
#saves the game
    data = {
        'inventory': inventory,
        'hp': HP,
        'gold': Gold,
        'Name': Name
    }
    with open(f"{Name}.json", 'w') as file:
        json.dump(data, file)


def start_game():
#Starts the game
    NewOrSave = input('New game or load save? ("new" or "load")')
    if NewOrSave == 'new':
        inventory = {}
        HP = 100
        Gold = 300
        Name = print_welcome()
    elif NewOrSave == 'load':
        Name = input('What is the name of the save?')
        Name, inventory, HP, Gold = load_game(Name)
    return Name, inventory, HP, Gold


def load_game(Name):
    # Loads a game if start game calls for load game, If loading fails it just starts a new cause it kept crashing without the "try"
    file_name = f"{Name}.json"
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if not content:  # Check if file is empty
                raise ValueError("Save file is empty.")
            data = json.loads(content)
            inventory = data.get('inventory', [])
            hp = data.get('hp', 100)
            gold = data.get('gold', 300)
            return Name, inventory, hp, gold
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f"Error loading save file: {e}")
        print("Starting a new game...")
        Name = print_welcome()
        return Name, [], 100, 300


def purchase_item(item_stats, Gold, item_choice, inventory, quantity=1):
    if item_choice not in item_stats:
        print("Item not found.")
        return Gold

    item_price = item_stats[item_choice]['price']
    item_durability = item_stats[item_choice]['durability']

    total_cost = item_price * quantity
    if Gold >= total_cost:
        Gold -= total_cost
        if item_choice in inventory:
            inventory[item_choice]['quantity'] += quantity
        else:
            inventory[item_choice] = {
                'quantity': quantity,
                'durability': item_durability
            }
        print("You bought {quantity} {item_choice}(s).")
    else:
        print("Not enough gold.")
    return Gold



def new_random_monster():
    
    """This is the list of monsters and their traits. A monster is selected with random and then given random traits and returned"""
    
    monster_dict = [
        {
        'name': 'Slime',
        'desc': 'A small clump of rotting biomatter clung together by the collective, dying will of its parts',
        'health': (1, 3),
        'power': (0, 2),
        'Gold': (5, 10)
    },
    {
        'name': 'Zombie',
        'desc': 'Any dead creature with enough soul left to continue to move',
        'health': (20, 50),
        'power': (10, 20),
        'Gold': (20, 60)
    },
    {
        'name': 'Greg',
        'desc': 'Greg is a wealthy passerby. Will you sacrifice your morality for wealth?',
        'health': (8, 12),
        'power': (1, 3),
        'Gold': (2000, 5000)
    }
    ]

    #This is the logic for creating a new monster using random

    monster = random.choice(monster_dict)
    return {
        'name': monster['name'],
        'desc': monster['desc'],
        'health': random.randint(*monster["health"]),
        'power': random.randint(*monster['power']),
        'Gold': random.randint(*monster['Gold'])
    }


#--------------------------------------------------------------------------------------------------------------------------------
# New functions for assignment 6 below line

def print_welcome():
    Name = input('What is your name?\n')

    print(f'Hello {Name}!')
    return(Name)

#This is outdated but I'm keeping it for now just in case I need it
SHOP_ITEMS = {
    'Bow': 125.75,
    'Arrow': 2.50,
    'Potion': 10.50,
    'Wand': 299.99,
    'Sword': 135.80,
    'Shield': 99.99
}


def print_shop_menu(item1Name, item1Price, item2Name, item2Price):

    """Prints the formatted shop
    
    
        item1Name: name of item 1
        item1Price: price of item 1
        item2Name: name of item2
        item2Price: price of item 2
    
       --To Do-- Add returns instead of just printing when the game has more structure and the values can be returned somewhere.
     """

def print_shop_menu():
    print("/---------------------\\")
    for item, stats in item_stats.items():
        print(f"| {item} ${stats['price']} |")
    print("\\---------------------/")

'''
Used to store the items the player buys
'''


inventory = {
    'Bow': 0,
    'Arrow': 0,
    'Potion': 0,
    'Wand': 0,
    'Sword': 0,
    'Shield': 0
}


item_stats = {
    "Sword": {"price": 100, "durability": 50, "multiplier": 3},
    "Bow": {"price": 100, "durability": 50, "multiplier": 4},
#    "Arrow": {"price": 2.5, "durability": 1, "multiplier": 0.5},  unused for now cause idk how to impliment 
    "Potion": {"price": 50, "durability": 1, "multiplier": 500},  
    "Wand": {"price": 200, "durability": 100, "multiplier": 3},
    "Shield": {"price": 99.99, "durability": 15, "multiplier": 0}, 
}

'''
Used to add items to the player inventory after they have been purchased
'''

def add_to_inventory(inventory, item, quantity=1):
    if item in inventory:
        inventory[item] += quantity
    else:
        print("Item {item} not recognized.")

'''
Used to remove items from the players inventory after they have been used.
'''


def remove_from_inventory(inventory, item, quantity=1):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
    else:
        print("Not enough {item} in inventory to remove.")



'''
Used when the players inventory needs to be displayed
'''

def display_inventory(inventory):
    print("\nInventory:")
    for item, data in inventory.items():
        quantity = data['quantity']
        durability = data['durability']
        print("- {item} (x{quantity}, Durability: {durability})")




'Manages fights between the player and monster returning the gold amount the monster dropped.'

def fight_manager(playerhealth = 50, playerdmg = 5, inventory = {}):

    monster = new_random_monster()
    monstername = monster['name']
    monsterhealth = monster['health']
    monsterdmg = monster['power']
    monstergold = monster['Gold']
    desc = monster['desc']
    

    choice = int(input('A wild {monstername} appeared! {desc}. Monster Health: {monsterhealth}, Monster Damage: {monsterdmg}, Gold Reward: {monstergold}. Fight(1), Run(2): '))
    
    # lets the player pick a weapon
    if inventory:
        print("\nChoose your weapon from the inventory:")
        for idx, item in enumerate(inventory):
            if item in item_stats:  # Make sure the item is real
                print("{idx + 1}. {item} (Durability: {item_stats[item]['durability']})")
        weapon_choice = int(input("Select your weapon: ")) - 1
        weapon = list(inventory.keys())[weapon_choice]  
        weapon_info = item_stats.get(weapon, None)  
        
        if weapon_info is None:
            print("Error: {weapon} does not have valid stats in item_stats.")
            return 0  
        
        weapon_dmg = weapon_info['multiplier']
        weapon_durability = weapon_info['durability']
        print('You equipped {weapon} with damage multiplier of {weapon_dmg} and durability of {weapon_durability}.\n')
    else:
        weapon_dmg = 1  # this is for if there is no weapon
        weapon_durability = 0

    # Combat loop
    while playerhealth > 0 and monsterhealth > 0 and choice == 1:
        # Calculate damage using weapon multiplier
        total_player_dmg = playerdmg * weapon_dmg  # Multiply base player damage by weapon multiplier
        monsterhealth -= total_player_dmg
        print('You dealt {total_player_dmg} damage. Monster health: {monsterhealth}')
        
        # Is the monster still alive?
        if monsterhealth > 0:
            playerhealth -= monsterdmg
            print('{monstername} attacks, dealing {monsterdmg} damage. Player health: {playerhealth}')
        
        # durraiblity - 1
        if weapon_durability > 0:
            weapon_durability -= 1
            print('{weapon} durability: {weapon_durability}')
            if weapon_durability <= 0:
                print('Your {weapon} broke!')
                del inventory[weapon]
                break


        # Continue or run away
        if monsterhealth > 0 and playerhealth > 0:
            choice = int(input('fight (1) run away (2): '))
            if choice != 1:
                print('You ran away!')
        else:
            break

    # End of fight conditions
    if monsterhealth <= 0 and playerhealth > 0:
        print('You won the fight! You got {monstergold} gold!')
        return monstergold
    elif playerhealth <= 0:
        print('You died')
        return 0
    elif choice != 1:
        print('You ran away!')
        return 0


    



def function_test_if_main():


    """This tests the functions if they are running in main"""
    print('This test shows what happens when the player does not have enough Gold to purchase an item\n')
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

    if __name__ == '__main__':
        function_test_if_main()