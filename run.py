import sys
import random

# print(
#     '''
#   ____       _______ _______ _      ______    _____ _    _ _____ _____   _____ 
#  |  _ \   /\|__   __|__   __| |    |  ____|  / ____| |  | |_   _|  __ \ / ____|
#  | |_) | /  \  | |     | |  | |    | |__    | (___ | |__| | | | | |__) | (___  
#  |  _ < / /\ \ | |     | |  | |    |  __|    \___ \|  __  | | | |  ___/ \___ \ 
#  | |_) / ____ \| |     | |  | |____| |____   ____) | |  | |_| |_| |     ____) |
#  |____/_/    \_\_|     |_|  |______|______| |_____/|_|  |_|_____|_|    |_____/ 
#     '''
# )


def welcome_message():
    '''
    Prints welcome message to user, asks if they want to play a game and
    collects user input
    '''
    while True:
        print('Would you like to play a game?')
        print('[y] = yes, [n] = no')

        player_answer = input('\n').lower()

        if validate_input(player_answer):
            break

    if player_answer == 'y':
        return True
    else:
        return False


def validate_input(user_input):
    '''
    Validates user input and returns True if it is valid or False if it is not
    '''
    try:
        if user_input == 'y' or user_input == 'n':
            return True
        else:
            raise Exception
    except Exception:
        print("Input must be 'y' or 'n', please try again\n")
        return False
    return True


def play_or_quit(play_game):
    '''
    Determines if user wants to play. If they don't, a goodbye message is
    printed. If they do, function returns to main()
    '''
    if play_game:
        return
    else:
        print(
            '''Closing game. If you change your mind, press the 'Run Program'
button above to restart the game''')
        sys.exit()


def get_player_name():
    '''
    Get and return user's name, defaulting to 'Player1' if nothing is entered.
    Function will validate to ensure name is no longer than 40 chars
    '''
    while True:
        try:
            player_name = input('Please enter your name (leave blank to use "Player1"): \n')
            if player_name == '':
                return 'Player1'
            elif len(player_name) > 40:
                print("My memory isn't that good, please choose something shorter")
                continue
            else:
                return player_name
        except Exception:
            print('There was an error with your name, please try again')


def show_instructions():
    '''
    Asks user if they want to see the rules and responds based on user input
    '''
    while True:
        print('Would you like to see the rules?')
        print('[y] = yes, [n] = no')

        player_answer = input('\n').lower()

        if validate_input(player_answer):
            break

    if player_answer == 'n':
        return
    else:
        print('''This version of battleships is played on a 6x6 board.
You will be given three ships of the same length to place on your board,
and your opponenet will do the same with their board. The objective is to sink
your opponent's ships by supplying the co-ordinates of where you think they
have placed their ships. The first player to sink all the opponent's ships
is the winner.

To keep track of your shots, you will be provided with a 'guess' board.
The symbols on the board are as follows:
~ = An untouched section of a board
+ = An undamaged section of a ship
@ = A section of a ship which has been hit
M = A shot which missed''')
        return


class Gameboard:
    '''
    Creates an instance of the Gameboard class which manages the board appearance,
    ship placement and player/computer guesses
    '''
    wave = '~'
    ship_section = '+'
    damaged_ship_section = '@'
    missed_shot = 'M'
    row_coordinates_key = ('a', 'b', 'c', 'd', 'e', 'f')

    def __init__(self, owner):
        self.rows = 6
        self.cols = 6
        self.board_contents = self.generate_blank_board()
        self.owner = owner
        self.ships = {'ship 1': [], 'ship 2': [], 'ship 3': []}


    def generate_blank_board(self):
        '''
        Generates a dictionary representing the board, with 6 rows
        each containing 6 values
        '''
        board_grid = {}

        for row in range(self.rows):
            for col in range(self.cols):
                board_grid.update({f'{Gameboard.row_coordinates_key[row]}{col}': Gameboard.wave})

        return board_grid

    def print_board(self):
        '''
        Prints the board contents to the terminal in a grid format
        '''
        # Add column numbers across top of board
        print('   0   1   2   3   4   5')

        # Adds border to top
        print(' -' * 13)

        # Prints each row starting with the row letter
        for row in range(self.rows):
            row_to_print = f'{Gameboard.row_coordinates_key[row]}' + '| '
            for col in range(self.cols):
                row_to_print += self.board_contents[f'{Gameboard.row_coordinates_key[row]}{col}'] + ' | '
            print(row_to_print)

        # Adds border to bottom
        print(' -' * 13)

    def create_ships(self, player):
        #TODO FIX ERROR WITH COMPUTER GENERATING SHIPS
        if player == 'comp':
            for ship in self.ships:
                while True:
                    ship_placement = self.generate_comp_input()
                    if validate_ship_input(ship_placement):
                        valid_placement, ship_coordinates, error_message = self.check_ship_placement(ship_placement)
                        if valid_placement:
                            self.ships[ship] = ship_coordinates
                            self.add_ship_to_board(self.ships[ship])
                            break
                self.print_board()

        else:
            for ship in self.ships:
                while True:
                    print(f'Where would you like to place {ship}?')
                    print('Enter the starting co-ordinates followed by V for vertical placement (top to bottom) or H for horizontal placement (left to right), e.g. A2H or C4V')
                    ship_placement = input().lower()
                    if validate_ship_input(ship_placement):
                        valid_placement, ship_coordinates, error_message = self.check_ship_placement(ship_placement)
                        if valid_placement:
                            self.ships[ship] = ship_coordinates
                            self.add_ship_to_board(self.ships[ship])
                            break
                        print(error_message)
            self.print_board()


    def check_ship_placement(self, ship_placement):
        '''
        Takes the co-ordinates as input by the user and splits it into a row,
        column and orientation. Takes the row and column to determine a starting
        position then cycles through each section of the ship (4) to checks that
        the co-ordiantes exist and that they don't contain another ship, using 
        the orienation to determine which co-ordinates to check.
        '''
        ship_row = ship_placement[0]
        # ship_row is a letter, find the index of that letter in the row_coordinates key
        # so letter can be increased in loops
        row_letter_index = Gameboard.row_coordinates_key.index(ship_row)
        # Convert ship column to int to allow iteration through each ship section
        ship_col = int(ship_placement[1])
        ship_orientation = ship_placement[2]
        active_board = self.board_contents

        # Checks available space is user has selected horizontal
        if ship_orientation == 'h':
            h_coordinates_list = []
            # Ships are 4 sections long
            for ship_section in range(4):
                active_pos_key = f'{ship_row}{ship_col}'

                # Check if co-ordinates for the ship section exist on the board
                if active_pos_key not in active_board:
                    error = "Not enough space for this ship, please provide a different location"
                    return False, h_coordinates_list, error

                # Get the contents of the board space where the ship_section is to be placed
                active_pos_contents = active_board[active_pos_key]

                # Check to make sure contents of the space are a 'wave'
                if active_pos_contents != Gameboard.wave:
                    error = "There is another ship in the way, please provide a different location"
                    return False, h_coordinates_list, error
                
                # Add ship_section to co-ordinates list
                h_coordinates_list.append(active_pos_key)

                # Increase ship_col by one so next ship_section is checked
                ship_col += 1
            return True, h_coordinates_list, None

        # Checks available space is user has selected vertical
        if ship_orientation == 'v':
            v_coordinates_list = []
            # Ships are 4 sections long
            for ship_section in range(4):
                active_pos_key = f'{Gameboard.row_coordinates_key[row_letter_index]}{ship_col}'

                # Check if co-ordinates for the ship section exist on the board
                if active_pos_key not in active_board:
                    error = "Not enough space for this ship, please provide a different location"
                    return False, v_coordinates_list, error

                # Get the contents of the board space where the ship_section is to be placed
                active_pos_contents = active_board[active_pos_key]

                # Check to make sure contents of the space are a 'wave'
                if active_pos_contents != Gameboard.wave:
                    error = "There is another ship in the way, please provide a different location"
                    return False, v_coordinates_list, error
                
                # Add ship_section to co-ordinates list
                v_coordinates_list.append(active_pos_key)

                # Increase ship_col by one so next ship_section is checked
                row_letter_index += 1
            return True, v_coordinates_list, None
    
    def add_ship_to_board(self, ship):
        for section in ship:
            self.board_contents[section] = '+'

    def generate_comp_input(self):
        row_letter = random.choice(Gameboard.row_coordinates_key)
        col_number = random.randint(0, 5)
        orientation = random.choice(('h','v'))
        comp_input = f'{row_letter}{col_number}{orientation}'
        return comp_input





def validate_ship_input(user_input):
    '''
    Validates users input for placing a ship to make sure it
    is the right length and uses only valid characters
    '''
    valid_row_inputs = ('a', 'b', 'c', 'd', 'e', 'f')
    valid_col_inputs = ('0', '1', '2', '3', '4', '5')
    valid_orientation = ('h', 'v')

    try:
        if len(user_input) < 3:
            print('Input too short, please try again')
            return False
        elif len(user_input) > 3:
            print('Input too long, please try again')
            return False
        elif user_input[0] not in valid_row_inputs:
            print('Invalid co-ordinates entered, please use only A-E and 0-5')
            return False
        elif user_input[1] not in valid_col_inputs:
            print('Invalid co-ordinates entered, please use only A-E and 0-5')
            return False
        elif user_input[2] not in valid_orientation:
            print('Invalid orientation entered, please use H or V')
            return False
        else:
            return True
    except Exception:
        print('There was an error with your input, please try again')
        return False

def main():
    '''
    Runs all the functions for the game
    '''
    player_response = welcome_message()
    play_or_quit(player_response)
    player_name = get_player_name()
    show_instructions()
    player_board = Gameboard(player_name)
    comp_board = Gameboard('Computer')
    player_board.print_board()
    comp_board.print_board()
    player_board.create_ships(player_name)
    comp_board.create_ships('comp')
    comp_board.generate_blank_board()
    # comp_board.create_ships('comp')
    # comp_board.generate_blank_board()
    # comp_board.create_ships('comp')
    # comp_board.generate_blank_board()
    # comp_board.create_ships('comp')
    # comp_board.generate_blank_board()
    print('code got back to main()')

main()
