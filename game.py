'''
This is the main game file that the game will actually run within. The functions will be imported from gamefunctions.py
and used here
'''
import gamefunctions

#had to move item stats to game.py for simplicity 

item_stats = {
    "Sword": {"price": 100, "durability": 50, "multiplier": 3},
    "Bow": {"price": 100, "durability": 50, "multiplier": 4},
    "Arrow": {"price": 2.5, "durability": 1, "multiplier": 0.5},
    "Potion": {"price": 50, "durability": 1, "multiplier": 500},  
    "Wand": {"price": 200, "durability": 100, "multiplier": 3},
    "Shield": {"price": 99.99, "durability": 15, "multiplier": 0}, 
}
    


def main():
    '''This is the main game function, everything should run within this'''
    money = 300
    inventory = {}
    name = str(input('What is your name?\n'))
    gamefunctions.print_welcome(name)



    while True:
        print("\nWhat would you like to do?\n")
        print("1. Shop")
        print("2. Fight")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':  # Shop
            gamefunctions.print_shop_menu()  # Print the shop menu with items and prices
            item_choice = input("What would you like to buy?\n")

            if item_choice in gamefunctions.SHOP_ITEMS:  # Check if the item is valid
                price = gamefunctions.SHOP_ITEMS[item_choice]
                quantity = int(input(f"How many {item_choice}s would you like to buy? "))
                money = gamefunctions.purchase_item(item_stats, money, item_choice, inventory, quantity)
                gamefunctions.display_inventory(inventory)  # Display updated inventory after purchase
            else:
                print("That item is not available in the shop.")



        elif choice == '2':
            money += gamefunctions.fight_manager(playerhealth=50, playerdmg=5, inventory=inventory)

        elif choice == '3':
            print(f'Goodbye')
            break

        else:
            print("That is not a valid number, please pick a listed number.")

if __name__ == "__main__":
    main()