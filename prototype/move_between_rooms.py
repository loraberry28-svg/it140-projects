"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting  room
current_room = "Great Hall"
while current_room != "exit":
    print("\nYou are in the", current_room)
    command = input("Enter your move: ").lower().strip()
    if command == "exit":
        current_room = "exit"
    elif command.startswith("go "):
        direction = command[3:].strip()
         if direction in rooms[current_room]:
             current_room = rooms[current_room] [direction]
             print("You moved to the", current_room)
         else:
             print("invalid direction. Try again.")
    else:
        print("invalid command. Try again.")
print("Thank you for playing")        


