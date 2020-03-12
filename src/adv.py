from room import Room
from player import Player
from colorama import Fore, Back, Style, init
from termcolor import colored

init()

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

input_list = ['n', 'e', 's', 'w', 'q']

# Make a new player object that is currently in the 'outside' room.
player = Player("Raajn", room["outside"])

user_input = ""
quit_game = False


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def input_instructions():
    print(Fore.LIGHTBLUE_EX + player.current_room.where_am_i())

    global user_input
    print(Fore.GREEN + "Where would you like to go? N, S, E, W? Type Q to Quit.")
    user_input = input()
    check_input(user_input)


def check_input(inp):
    if inp in input_list:
        move_player(inp)
    else:
        print(Fore.RED + "Incorrect Input. Please Try Again!")


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

def move_player(inp):
    global quit_game
    global player
    if inp == "q":
        print(Fore.YELLOW + 'Thanks for playing!')
        quit_game = True
    else:
        possible_room = getattr(player.current_room, f"{inp}_to")
        # print(possible_room)
        if possible_room is None:
            print(Fore.RED + "There is nothing in that direction.  You have not moved.")
            print(Fore.GREEN + "Where would you like to go? N, S, E, W? Type Q to Quit.")
            user_input = input()
            check_input(user_input)
        else:
            player.current_room = possible_room


# If the user enters "q", quit the game.

while True:

    input_instructions()

    if quit_game:
        break
