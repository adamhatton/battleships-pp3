import os
import sys
import random
from time import sleep

print(
    '''
  ____       _______ _______ _      ______    _____ _    _ _____ _____   _____
 |  _ \   /\|__   __|__   __| |    |  ____|  / ____| |  | |_   _|  __ \ / ____|
 | |_) | /  \  | |     | |  | |    | |__    | (___ | |__| | | | | |__) | (___
 |  _ < / /\ \ | |     | |  | |    |  __|    \___ \|  __  | | | |  ___/ \___ \\
 | |_) / ____ \| |     | |  | |____| |____   ____) | |  | |_| |_| |     ____) |
 |____/_/    \_\_|     |_|  |______|______| |_____/|_|  |_|_____|_|    |_____/
    '''
)


def play_message(game):
    '''
    Prints message to user, asks if they want to play a game and
    collects user input
    '''
    while True:
        if game == 'first':
            typed_print('Would you like to play a game?\n')
        else:
            typed_print('Would you like to play again?')
        player_answer = typed_input('[y] = yes, [n] = no\n').lower()

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
        typed_print("Input must be 'y' or 'n', please try again\n")
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
        typed_print('''
Closing game. If you change your mind, press the 'Run Program'
button above to restart the game''')
        sys.exit()


def get_player_name():
    '''
    Get and return user's name, defaulting to 'Player1' if nothing is entered.
    Function will validate to ensure name is no longer than 40 chars
    '''
    while True:
        try:
            player_name = typed_input('''
Please enter your name (leave blank to use "Player1"): \n''')
            if player_name == '':
                return 'Player1'
            elif len(player_name) > 18:
                typed_print('''
My memory isn't that good, please choose something
shorter''')
                continue
            else:
                return player_name
        except Exception:
            typed_print('There was an error with your name, please try again')


def show_instructions(player_name):
    '''
    Asks user if they want to see the rules and responds based on user input
    '''
    while True:
        clear_console()
        print(f'\nWelcome {player_name}')
        typed_print('Would you like to see the rules?\n')
        player_answer = typed_input('[y] = yes, [n] = no\n').lower()

        if validate_input(player_answer):
            break

    if player_answer == 'n':
        return
    else:
        clear_console()
        print('''
  _____  _    _ _      ______  _____
 |  __ \| |  | | |    |  ____|/ ____|
 | |__) | |  | | |    | |__  | (___
 |  _  /| |  | | |    |  __|  \___ \\
 | | \ \| |__| | |____| |____ ____) |
 |_|  \_\\_____/|______|______|_____/
        ''')
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

        input('\nPress any key to continue\n')
        return


def game_start_text():
    clear_console()
    print('''
   _____          __  __ ______    _____ _______       _____ _______
  / ____|   /\   |  \/  |  ____|  / ____|__   __|/\   |  __ \__   __|
 | |  __   /  \  | \  / | |__    | (___    | |  /  \  | |__) | | |
 | | |_ | / /\ \ | |\/| |  __|    \___ \   | | / /\ \ |  _  /  | |
 | |__| |/ ____ \| |  | | |____   ____) |  | |/ ____ \| | \ \  | |
  \_____/_/    \_\_|  |_|______| |_____/   |_/_/    \_\_|  \_\ |_|
    ''')

    input('\nPress any key to continue\n')
    return


def commence_attack_text():
    clear_console()
    print('''
   _____ ____  __  __ __  __ ______ _   _  _____ ______
  / ____/ __ \|  \/  |  \/  |  ____| \ | |/ ____|  ____|
 | |   | |  | | \  / | \  / | |__  |  \| | |    | |__
 | |   | |  | | |\/| | |\/| |  __| | . ` | |    |  __|
 | |___| |__| | |  | | |  | | |____| |\  | |____| |____
  \_____\____/|_|  |_|_|  |_|______|_| \_|\_____|______|

        _______ _______       _____ _  __
     /\|__   __|__   __|/\   / ____| |/ /
    /  \  | |     | |  /  \ | |    | ' /
   / /\ \ | |     | | / /\ \| |    |  <
  / ____ \| |     | |/ ____ \ |____| . \\
 /_/    \_\_|     |_/_/    \_\_____|_|\_\\
    ''')
    input('\nPress any key to continue\n')
    clear_console()
    return


class Gameboard:
    '''
    Creates an instance of the Gameboard class which manages the board
    appearance, ship placement and player/computer guesses
    '''
    wave = '~'
    ship_section = '+'
    damaged_ship_section = '@'
    missed_shot = 'M'
    row_coords_key = ('a', 'b', 'c', 'd', 'e', 'f')

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
                coord = f'{Gameboard.row_coords_key[row]}{col}'
                board_grid.update({coord: Gameboard.wave})

        return board_grid

    def print_board(self):
        '''
        Prints the board contents to the terminal in a grid format
        '''
        # Add column numbers across top of board
        print('{:^26}'.format(f"{self.owner}'s Board"))
        print('   0   1   2   3   4   5')

        # Adds border to top
        print(' -' * 13)

        # Prints each row starting with the row letter
        for row in range(self.rows):
            row_to_print = f'{Gameboard.row_coords_key[row]}' + '| '
            for col in range(self.cols):
                coord = f'{Gameboard.row_coords_key[row]}{col}'
                row_to_print += self.board_contents[coord] + ' | '
            print(row_to_print)

        # Adds border to bottom
        print(' -' * 13)

    def print_both_boards(self, guess_board):
        '''
        Prints player's board and their guess board to
        the terminal in a grid format
        '''
        clear_console()
        left_number_headings = '  0   1   2   3   4   5'
        right_number_headings = '   0   1   2   3   4   5'
        border = ' -' * 13

        # Prints board titles
        print('{:^26}{:10}{:^26}'.format(
            f"{self.owner}'s Board", '', f"{guess_board.owner}'s Board"))
        # Prints board headings
        print('{:^26}{:10}{:^26}'.format(
            left_number_headings, '', right_number_headings))
        # Prints border to top of board
        print('{:^26}{:10}{:^26}'.format(border, '', border))

        # Generates and prints each row by combining info from both boards
        for row in range(self.rows):
            l_row_to_prt = f'{Gameboard.row_coords_key[row]}' + '| '
            r_row_to_prt = f'{Gameboard.row_coords_key[row]}' + '| '
            for col in range(self.cols):
                coord = f'{Gameboard.row_coords_key[row]}{col}'
                l_row_to_prt += self.board_contents[coord] + ' | '
                if guess_board.board_contents[coord] == '+':
                    r_row_to_prt += '~' + ' | '
                else:
                    r_row_to_prt += guess_board.board_contents[coord] + ' | '
            print('{:^26}{:10}{:^26}'.format(l_row_to_prt, '', r_row_to_prt))

        # Adds border to bottom
        print('{:^26}{:10}{:^28}'.format(border, '', border))

    def create_ships(self):
        '''
        Gets user input and if valid uses it to create ships to the
        Gameboard.ships attribute. Calls add_ship_to_board
        to update board contents with ships. For the computer board
        the input is randomly generated.
        '''
        for ship in self.ships:
            clear_console()
            while True:
                if self.owner != 'Computer':
                    self.print_board()
                    typed_print(f'''
Where would you like to place {ship}? (Length = 4)\n''')
                    print('''
Enter the starting co-ordinates followed by V for vertical placement (top to
bottom) or H for horizontal placement (left to right), e.g. A2H or C4V''')
                    ship_placement = input().lower()
                else:
                    ship_placement = self.generate_comp_input('placing')
                if self.validate_coords(ship_placement, 'placing'):
                    valid_placement, ship_coordinates, error_message =\
                        self.check_ship_placement(ship_placement)
                    if valid_placement:
                        self.ships[ship] = ship_coordinates
                        self.add_ship_to_board(self.ships[ship])
                        if self.owner != 'Computer':
                            self.print_board()
                        break
                    if self.owner != 'Computer':
                        print(error_message)

    def check_ship_placement(self, ship_placement):
        '''
        Takes the co-ordinates as input by the user and splits it into a row,
        column and orientation. Takes the row and column to determine a
        starting position then cycles through each section of the ship (4)
        to check that the co-ordiantes exist and that they don't contain
        another ship, using the orienation to determine which co-ordinates
        to check.
        '''
        ship_row = ship_placement[0]
        # ship_row is a letter, find the index of that letter in the
        # row_coords key so letter can be increased in loops
        row_letter_index = Gameboard.row_coords_key.index(ship_row)
        # Convert ship col to int to allow iteration through each section
        ship_col = int(ship_placement[1])
        ship_orientation = ship_placement[2]
        active_board = self.board_contents
        coordinates_list = []

        for ship_section in range(4):
            coord = f'{Gameboard.row_coords_key[row_letter_index]}{ship_col}'
            active_pos_key = coord if row_letter_index < 6 else 'blank'

            # Check if co-ordinates for the ship section exist on the board
            if active_pos_key not in active_board:
                error = "Not enough space, please provide a different location"
                return False, coordinates_list, error

            # Get contents of board space where ship_section is to be placed
            active_pos_contents = active_board[active_pos_key]

            # Check to make sure contents of the space are a 'wave'
            if active_pos_contents != Gameboard.wave:
                clear_console()
                error = '''
There is another ship in the way, please provide a different location'''
                return False, coordinates_list, error

            # Add ship_section to co-ordinates list
            coordinates_list.append(active_pos_key)

            # Increase ship_col by one so next ship_section is checked
            if ship_orientation == 'h':
                ship_col += 1
            elif ship_orientation == 'v':
                row_letter_index += 1
        return True, coordinates_list, None

    def add_ship_to_board(self, ship):
        '''
        Updates the Gameboard.board_contents with
        ships generated by create_ships()
        '''
        for section in ship:
            self.board_contents[section] = '+'

    def generate_comp_input(self, phase):
        '''
        Creates a random input to use for creating
        the computer's ships
        '''
        row_letter = random.choice(Gameboard.row_coords_key)
        col_number = random.randint(0, 5)
        orientation = random.choice(('h', 'v'))

        if phase == 'placing':
            comp_input = f'{row_letter}{col_number}{orientation}'
        elif phase == 'firing':
            comp_input = f'{row_letter}{col_number}'
        return comp_input

    def validate_coords(self, user_input, phase):
        '''
        Validates co-ordinates input by user to make sure they
        are the right length and use only valid characters
        '''
        valid_row_inputs = ('a', 'b', 'c', 'd', 'e', 'f')
        valid_col_inputs = ('0', '1', '2', '3', '4', '5')
        valid_orientation = ('h', 'v')
        input_len = 0

        if phase == 'firing':
            input_len = 2
        elif phase == 'placing':
            input_len = 3

        try:
            if len(user_input) < input_len:
                print('Input too short, please try again')
                return False
            if len(user_input) > input_len:
                print('Input too long, please try again')
                return False
            if user_input[0] not in valid_row_inputs:
                print('Invalid co-ordinates, please use only A-E and 0-5')
                return False
            if user_input[1] not in valid_col_inputs:
                print('Invalid co-ordinates, please use only A-E and 0-5')
                return False
            if phase == 'placing':
                if user_input[2] not in valid_orientation:
                    print('Invalid orientation entered, please use H or V')
                    return False
            return True
        except Exception as e:
            print(f'There was an error with your input: {e}. Please try again')
            return False

    def fire_shot(self, defending_board):
        '''
        Takes an input, fires a shot at the provided co-ordinates,
        then calls update_board_with_shot for shot feedback
        '''
        while True:
            if self.owner != 'Computer':
                print('Where do you want to fire?')
                print('Enter the co-ordinates e.g. B4 or E0')
                shot_coords = input().lower()
            else:
                shot_coords = self.generate_comp_input('firing')

            if self.validate_coords(shot_coords, 'firing'):
                if defending_board.update_board_with_shot(shot_coords, self):
                    break
                if self.owner != 'Computer':
                    print('''
You have already fired at this location, please enter different
co-ordinates''')

    def update_board_with_shot(self, shot_coords, attacking_board):
        '''
        Takes a shot and updates the board_contents to
        show where a shot has landed. Prints out a message
        to user of where shot landed
        '''
        if (self.board_contents[shot_coords] == 'M' or
                self.board_contents[shot_coords] == '@'):
            return False

        if self.board_contents[shot_coords] == '+':
            print(f'''
{attacking_board.owner} fired at {shot_coords} and got a direct hit on
{self.owner}!''')
            self.board_contents[shot_coords] = '@'
            sleep(1.5)
            return True

        print(f'''
{attacking_board.owner} fired at {shot_coords} missed all of
{self.owner}'s ships!''')
        self.board_contents[shot_coords] = 'M'
        sleep(1.5)
        return True

    def check_for_win(self, defending_board):
        if '+' not in defending_board.board_contents.values():
            print(f'''
{self.owner} has destroyed all of {defending_board.owner}'s ships!''')
            return True
        return False

    def reset_variables(self):
        '''
        Resets the Gameboard variables that can change during the game
        '''
        self.board_contents = self.generate_blank_board()
        self.ships = {'ship 1': [], 'ship 2': [], 'ship 3': []}


# Code taken from https://www.delftstack.com/howto/python/python-clear-console/
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
# End of code taken from delftstack.com


# Code taken from https://www.101computing.net/python-typing-text-effect/
def typed_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.02)


def typed_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.02)
    value = input()
    return value
# End of code taken from 101computing.net


def main():
    '''
    Runs all the functions for the game
    '''
    player_response = play_message('first')
    play_or_quit(player_response)
    player_name = get_player_name()
    show_instructions(player_name)
    game_start_text()
    player_board = Gameboard(player_name)
    comp_board = Gameboard('Computer')

    while True:
        player_board.create_ships()
        comp_board.create_ships()
        commence_attack_text()
        player_board.print_both_boards(comp_board)

        while True:
            player_board.fire_shot(comp_board)
            player_board.print_both_boards(comp_board)
            if player_board.check_for_win(comp_board):
                break

            comp_board.fire_shot(player_board)
            player_board.print_both_boards(comp_board)
            if comp_board.check_for_win(player_board):
                break

        player_response = play_message('rematch')
        play_or_quit(player_response)
        player_board.reset_variables()
        comp_board.reset_variables()
    print('code got back to main()')


main()
