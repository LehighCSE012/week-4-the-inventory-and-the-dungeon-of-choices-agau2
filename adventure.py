"""
The follwing code uses functions to execute the adventure from Week 3 and extends
it with Week 4 content.
"""

import random #In order to use random.choice() and random.random()

def acquire_item(inventory, item):
    """Appends the item to the inventory list."""
    added_to_inventory = []
    if item:
        #The .append() function will add an item into aquired_items as the last element.
        inventory.append(item)
        #The + is list concatenation, so the items of inventory get copied into added_to_inventory
        added_to_inventory = added_to_inventory + inventory
        print(f"You found a {item} in the room!")
    return added_to_inventory

def display_inventory(inventory):
    """This function will display and format the player's inventory list."""
    number = 1
    if inventory:
        print("Your inventory:")
        #The in operator takes every element inventory and assigns them to item
        for item in inventory:
            print(f"{number}. {item}")
            number += 1
    else:
        print("Your inventory is empty.")

def display_player_status(player_health):
    """Prints the player's current health to the console in a user-friendly format."""

    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Randomly chooses a path for the player."""

    player_path = random.choice(["left","right"])
    if player_path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health += 10
        player_health = min(player_health, 100)
    if player_path == "right":
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """Simulates the player's attack."""

    print("You strike the monster for 15 damage!")
    updated_monster_health = monster_health - 15
    return updated_monster_health

def monster_attack(player_health):
    """Simulates the monster's attack."""

    critical_num = random.random() #Generates number between (0,1)
    if critical_num < 0.5:
        print("The monster lands a critical hit for 20 damage!")
        updated_player_health = player_health - 20
    else:
        print("The monster hits you for 10 damage!")
        updated_player_health = player_health - 10
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Manages the combat encounter using a while loop."""

    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            break
        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("Game Over!")
            has_treasure = False
            break
        display_player_status(player_health)
    return has_treasure # boolean

def check_for_treasure(has_treasure):
    """Checks the value of has_treasure."""

    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Iterates through each room in dungeon_rooms and prints the room_description."""

    updated_inventory = []
    #The in operator takes every element of dungeon_rooms and assigns them to room
    for room in dungeon_rooms:
        print(room[0])
        if room[1]:
            updated_inventory = acquire_item(inventory, room[1])
        if room[2] == "puzzle":
            print("You encouter a puzzle!")
            puzzle_decision = input("Would you like to solve or skip the puzzle?")
            if puzzle_decision == "solve":
                puzzle_success = random.choice([True, False])
                if puzzle_success:
                    print(room[3][0])
                    player_health = player_health - room[3][2]
                else:
                    print(room[3][1])
                    player_health = player_health + room[3][2] 
                if player_health < 0:
                    player_health = 0
                    print("You are barely alive!")
        if room[2] == "trap":
            print("You see a potential trap!")
            trap_decision = input("Do you want to disarm or bypass the trap?")
            if trap_decision == "disarm":
                trap_success = random.choice([True, False])
                if trap_success:
                    print(room[3][0])
                    player_health = player_health - room[3][2]
                else:
                    print(room[3][1])
                    player_health = player_health + room[3][2]
                if player_health < 0:
                    player_health = 0
                    print("You are barely alive!")
        if room[2] == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
            player_health += 0

        display_inventory(updated_inventory)
        display_player_status(player_health)
    """
    try:
        #The del method will take the element in index 1 of room and remove it from room
        del dungeon_rooms[0][1] #Here, we try to remove the item from the first room
    except TypeError:
        print('''Error: Tuples like room in dungeon_rooms are immutable.
        This means that the rooms cannot be changed once they are defined.
        Thus, del dungeon_rooms[0][1] produces an error.''')
    """
    return player_health, updated_inventory

def main():
    """Executes the adventure using all previously defined functions."""
    player_health = 100
    monster_health = 70 # Example hardcoded value
    has_treasure = False
    inventory = []
    dungeon_rooms = [
        ("Where potions are brewed.", "potion", "trap", ("You escape an exposion!",
            "You're caught in an explosion.", -15)),
        ("A secret room hidden behind a false wall", "Rare Gem", "none", None),
        ("A chamber filled with jewels", "Golden Crown", "puzzle", ("You solve the puzzle!",
            "You don't solve the puzzle and take damage", -10)),
        ("A dark, damp cell with rusty chains", None, "none", None)]

    has_treasure = random.choice([True, False]) # Randomly assign treasure

    new_player_health = handle_path_choice(player_health)

    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic

    if new_player_health > 0:
        enter_dungeon(new_player_health, inventory, dungeon_rooms)

#Will run the main function
if __name__ == "__main__":
    main()
