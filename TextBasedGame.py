# Jeremy Palmer

# Show instructions function
def show_instructions():
    # print a main menu and the commands
    print("Dracula Text Game")
    print("Collect 6 items to win the game, or be destroyed by Dracula.")
    print("Move commands: South, North, East, West")
    print("Add to Inventory: get 'item name'")
    print("Type quit to exit the game")


# Function to display the player's inventory
def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item in inventory:
            print("- " + item)


# Function to move rooms
def move_rooms(current_room, direction, room_map):
    new_room = room_map[current_room][direction]
    return new_room


# Function to get item
def get_item(rooms_map, current_room):
    item_in_room = []
    for item, room in rooms_map[current_room].items():
        if item == "Item":
            item_in_room.append(room)
    return item_in_room


# Function that deletes item from room after it is picked up
def remove_item_from_room(room_map, current_room, item):
    if 'Item' in room_map[current_room] and room_map[current_room]['Item'] == item:
        del room_map[current_room]['Item']


# Define rooms and their connections
room_map = {
    'Dungeon': {'South': 'Library'},
    'Library': {'North': 'Dungeon', 'West': 'Great Hall', 'Item': 'Bible'},
    'Great Hall': {'East': 'Library', 'West': 'Bedroom', 'South': 'Dining Room', 'North': 'Trophy Room',
                   'Item': 'Crucifix'},
    'Bedroom': {'East': 'Great Hall', 'Item': 'Gun'},
    'Dining Room': {'North': 'Great Hall', 'East': 'Kitchen', 'Item': 'Holy water'},
    'Kitchen': {'West': 'Dining Room', 'Item': 'Garlic'},
    'Trophy Room': {'South': 'Great Hall', 'East': 'Throne Room', 'Item': 'Stake'},
    'Throne Room': {'West': 'Trophy Room', 'Boss': 'Dracula'}
}

# Player inventory list
inventory = []

# Set starting room
current_room = 'Dungeon'

# Tracks last move
direction = ''

show_instructions()

__name__ = "__main__"
# Game Loop
while True:
    # Display player info
    print(f"\nYou are in the {current_room}\nInventory : {inventory}\n{'-' * 27}")
    # Shows room and possible moves
    possible_moves = [move for move in room_map[current_room].keys() if move != 'Item' and move != 'Boss']
    print('Possible moves:', ', '.join(possible_moves))
    # Display available items in the room
    items_in_room = get_item(room_map, current_room)
    # Doesn't display item if it is in the players inventory
    items_to_display = [item for item in items_in_room if item.lower() not in [inv_item.lower() for inv_item in inventory]]
    if items_to_display:
        print(f'You see the following items in the room: {", ".join(items_to_display)}')
    # Get user input
    user_input = input("Choose a direction or type 'get [item]' to pick up an item: ").strip().capitalize()

    # Check if valid
    if user_input == 'Quit':
        break
    elif user_input in room_map[current_room]:
        # Move to room
        current_room = move_rooms(current_room, user_input, room_map)
    elif user_input.startswith('Get '):
        item_name = user_input[4:].lower()  # Extract item name from input and convert to lowercase
        if item_name in [item.lower() for item in items_in_room]:  # Compare the names
            if item_name not in [item.lower() for item in inventory]:
                inventory.append(item_name)
                print(f'You picked up {item_name}.')
                remove_item_from_room(room_map, current_room, item_name)
                # Print updated inventory
                display_inventory(inventory)
            else:
                print(f'You already have the {item_name} in your inventory.')    
        else:
            print(f'{item_name} is not in this room.')
    else:
        # Invalid input
        print('Invalid input')
        
   # Dracula Encounter
    if 'Boss' in room_map[current_room].keys():
        # Lose
        if len(inventory) < 6:
            print(f"{room_map[current_room]['Boss']} drinks your blood.")
            break
        # Win
        else:
            print(f"You defeated {room_map[current_room]['Boss']} and ended his madness!")
            break
