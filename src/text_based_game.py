# Lora Berry
# IT-140 Project Two: Warehouse Mystery Text-Based Game


def show_instructions():
    """Display the story, objective, and available player commands."""
    print('Warehouse Mystery Text Adventure Game')
    print('Find all 6 pieces of evidence before encountering the Warehouse Thief!')
    print('Move commands: go north, go south, go east, go west')
    print('Collect an item: get <item name>')
    print('-' * 50)


def show_status(current_room, inventory, rooms):
    """Display the player's location, inventory, and available item."""
    print(f'\nYou are in the {current_room}')
    print(f'Inventory: {inventory}')
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print('-' * 50)


def main():
    """Run the warehouse investigation until the player wins or loses."""
    # Each room lists the accessible rooms and its evidence item, if any.
    rooms = {
        'Inventory Office': {'north': 'Receiving Area', 'east': 'Break Room',
                             'south': 'Shipping Area', 'west': 'Storage Area'},
        'Receiving Area': {'south': 'Inventory Office', 'east': 'Freezer',
                           'item': 'Shipping Manifest'},
        'Freezer': {'west': 'Receiving Area', 'item': 'Dropped Keycard'},
        'Break Room': {'west': 'Inventory Office', 'north': 'Security Office',
                       'item': 'Cell Phone'},
        'Shipping Area': {'north': 'Inventory Office', 'east': 'Manager\'s Office',
                          'item': 'Torn Shipping Label'},
        'Storage Area': {'east': 'Inventory Office', 'item': 'Flashlight'},
        'Security Office': {'south': 'Break Room', 'item': 'Security Footage'},
        "Manager's Office": {'west': 'Shipping Area'},  # Villain's room
    }

    current_room = 'Inventory Office'
    inventory = []
    villain_room = "Manager's Office"
    total_items = sum('item' in room for room in rooms.values())

    show_instructions()

    # Repeat until the player has won or entered the villain's room too soon.
    while True:
        show_status(current_room, inventory, rooms)
        command = input('Enter your move: ').strip()
        command_lower = command.lower()

        if command_lower.startswith('go '):
            direction = command_lower[3:].strip()
            if direction in rooms[current_room]:
                # Only directions are valid movement connections.
                if direction in ('north', 'south', 'east', 'west'):
                    current_room = rooms[current_room][direction]
                    if current_room == villain_room:
                        print('\nThe Warehouse Thief caught you! GAME OVER!')
                        print('Thanks for playing Warehouse Mystery!')
                        break
                else:
                    print('Invalid direction. Try north, south, east, or west.')
            else:
                print('You cannot go that way. Try another direction.')

        elif command_lower.startswith('get '):
            item_name = command[4:].strip()
            room_item = rooms[current_room].get('item')
            if room_item and item_name.lower() == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]['item']
                print(f'You collected the {room_item}!')
                if len(inventory) == total_items:
                    print('\nCongratulations! You collected all 6 pieces of evidence!')
                    print('You solved the Warehouse Mystery and defeated the thief!')
                    print('Thanks for playing Warehouse Mystery!')
                    break
            else:
                print('Invalid item. There is no matching item to collect here.')

        else:
            print('Invalid command. Use "go <direction>" or "get <item name>".')


if __name__ == '__main__':
    main()

