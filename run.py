'''
Contains Gameboard class and game functions
'''
import sys
import random
from time import sleep
import titles


def play_message(game):
    '''
    Prints message to user, asks if they want to play a game and
    collects user input
    '''
    while True:
        if game == 'first':
            typed_print('Would you like to play a game?\n')
        else:
            typed_print('\nWould you like to play again?\n')
        player_answer = typed_input('[y] = yes, [n] = no\n').lower()

        if validate_input(player_answer):
            break

    if player_answer == 'y':
        return True

    return False


def validate_input(user_input):
    '''
    Validates user input and returns True if it is valid or False if it is not
    '''
    try:
        if user_input in ('y', 'n'):
            return True
        raise Exception
    except Exception:
        typed_print("Input must be 'y' or 'n', please try again\n")
        sleep(1.1)
        return False
    return True


def play_or_quit(play_game):
    '''
    Determines if user wants to play. If they don't, a goodbye message is
    printed. If they do, function returns to main()
    '''
    if play_game:
        return

    typed_print('''
Closing game. If you change your mind, press the 'Run Program'
button above to restart the game\n''')
    sys.exit()


def get_player_name():
    '''
    Gets and returns user's name, defaulting to 'Player 1' if nothing is
    entered. Function will validate to ensure name is no longer than 18 chars
    '''
    while True:
        try:
            player_name = typed_input('''
Please enter your name (leave blank to use "Player 1"): \n''').strip()
            if player_name == '':
                return 'Player 1'
            if len(player_name) > 18:
                typed_print('''
My memory isn't that good, please choose something shorter''')
                continue
            return player_name
        except Exception:
            typed_print('There was an error with your name, please try again')


def show_instructions(player_name):
    '''
    Asks user if they want to see the rules and responds based on input
    '''
    while True:
        titles.clear_console()
        print(f'\nWelcome {player_name}')
        typed_print('Would you like to see the rules?\n')
        player_answer = typed_input('[y] = yes, [n] = no\n').lower()

        if validate_input(player_answer):
            break

    if player_answer == 'n':
        return
    titles.rules()


class Gameboard:
    '''
    Creates an instance of the Gameboard class which manages the board
    appearance, ship placement and player/computer guesses
    '''
    ROW_COORDS_KEY = ('a', 'b', 'c', 'd', 'e', 'f')

    def __init__(self, owner):
        self.rows = 6
        self.cols = 6
        self.board_contents = self.generate_blank_board()
        self.owner = owner
        self.ships = {
            'cruiser': ['', ''], 'submarine': ['', '', ''],
            'destroyer': ['', '', '', '']
        }
        self.ships_status = {
            'cruiser': 'active', 'submarine': 'active',
            'destroyer': 'active'
        }

    def generate_blank_board(self):
        '''
        Generates a dictionary representing the board, with 6 rows
        each containing 6 values
        '''
        board_grid = {}

        for row in range(self.rows):
            for col in range(self.cols):
                coord = f'{Gameboard.ROW_COORDS_KEY[row]}{col}'
                board_grid.update({coord: '~'})
        return board_grid

    def print_board(self):
        '''
        Prints the board contents to the terminal in a grid format
        '''
        # Add board owner's name to top of board
        print('{:^26}'.format(f"{self.owner}'s Board"))
        # Add column numbers across top of board
        print('   0   1   2   3   4   5')

        # Adds border to top
        print(' -' * 13)

        # Prints each row starting with the row letter
        for row in range(self.rows):
            row_to_print = f'{Gameboard.ROW_COORDS_KEY[row]}' + '| '
            for col in range(self.cols):
                coord = f'{Gameboard.ROW_COORDS_KEY[row]}{col}'
                row_to_print += self.board_contents[coord] + ' | '
            print(row_to_print)

        # Adds border to bottom
        print(' -' * 13)

    def print_both_boards(self, guess_board):
        '''
        Prints player's board and their guess board to
        the terminal in a grid format
        '''
        titles.clear_console()
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
            l_row_to_prt = f'{Gameboard.ROW_COORDS_KEY[row]}' + '| '
            r_row_to_prt = f'{Gameboard.ROW_COORDS_KEY[row]}' + '| '
            for col in range(self.cols):
                coord = f'{Gameboard.ROW_COORDS_KEY[row]}{col}'
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
        Gets user input and if valid uses it to add ships to the
        Gameboard.ships attribute. Calls add_ship_to_board
        to update board contents with ships. For the computer board
        the input is randomly generated.
        '''
        for ship, ship_coords in self.ships.items():
            while True:
                titles.clear_console()
                ship_len = len(ship_coords)
                # Get user input
                if self.owner != 'Computer':
                    self.print_board()
                    typed_print(f'''
Where would you like to place your {ship.capitalize()}? (Length = {ship_len})
''')
                    print('''
Enter the starting co-ordinates followed by V for vertical placement (top to
bottom) or H for horizontal placement (left to right), e.g. A2H or C4V:''')
                    ship_placement = input().lower()
                # Generate computer input
                else:
                    ship_placement = self.generate_comp_input('placing')
                # Validate that input is in correct format
                if self.validate_coords(ship_placement, 'placing'):
                    # Validate that ship can be placed at input coords
                    valid_placement, ship_coordinates, error_message =\
                        self.check_ship_placement(ship_len, ship_placement)
                    # Update Gameboard with the ship
                    if valid_placement:
                        self.ships[ship] = ship_coordinates
                        self.add_ship_to_board(self.ships[ship])
                        if self.owner != 'Computer':
                            self.print_board()
                        break
                    if self.owner != 'Computer':
                        print(error_message)
                        sleep(1.4)

    def check_ship_placement(self, ship_len, ship_placement):
        '''
        Takes the co-ordinates as input by the user and splits it into a row,
        column and orientation. Takes the row and column to determine a
        starting position then cycles through each section of the ship
        to check that the co-ordiantes exist and that they don't contain
        another ship, using the orienation to determine which co-ordinates
        to check.
        '''
        ship_row = ship_placement[0]
        # ship_row is a letter, find the index of that letter in the
        # row_coords key so letter can be increased in loops
        row_letter_index = Gameboard.ROW_COORDS_KEY.index(ship_row)
        # Convert ship col to int to allow iteration through each section
        ship_col = int(ship_placement[1])
        ship_orientation = ship_placement[2]
        active_board = self.board_contents
        # Create empty list to store ship coords. This is returned so it
        # can be used to update the Instance's ships attribute
        coordinates_list = []

        for ship_section in range(ship_len):
            active_pos_key = (
                f'{Gameboard.ROW_COORDS_KEY[row_letter_index]}{ship_col}' if
                row_letter_index < 6 else 'blank')

            # Check if co-ordinates for the ship section exist on the board
            if active_pos_key not in active_board:
                error = "Not enough space, please enter a different location\n"
                return False, coordinates_list, error

            # Get contents of board space where ship_section is to be placed
            active_pos_contents = active_board[active_pos_key]

            # Check to make sure contents of the space are a 'wave'
            if active_pos_contents != '~':
                error = '''
There is another ship in the way, please provide a different location\n'''
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
        the computer's ships based on the phase
        '''
        row_letter = random.choice(Gameboard.ROW_COORDS_KEY)
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
                print('\nInput too short, please try again')
                sleep(1.1)
                return False
            if len(user_input) > input_len:
                print('\nInput too long, please try again')
                sleep(1.1)
                return False
            if user_input[0] not in valid_row_inputs:
                print('\nInvalid co-ordinates, please use only A-E and 0-5')
                sleep(1.1)
                return False
            if user_input[1] not in valid_col_inputs:
                print('\nInvalid co-ordinates, please use only A-E and 0-5')
                sleep(1.1)
                return False
            if phase == 'placing':
                if user_input[2] not in valid_orientation:
                    print('\nInvalid orientation entered, please use H or V')
                    sleep(1.1)
                    return False
            return True
        except Exception as e:
            print(f'\nError with your input: {e}. Please try again')
            sleep(1.1)
            return False

    def fire_shot(self, defending_board):
        '''
        Takes an input, fires a shot at the provided co-ordinates,
        then calls update_board_with_shot for shot feedback
        '''
        while True:
            # Get user input
            if self.owner != 'Computer':
                print('\nWhere do you want to fire?')
                print('Enter the co-ordinates e.g. B4 or E0')
                shot_coords = input().lower()
            # Generate Computer input
            else:
                shot_coords = self.generate_comp_input('firing')

            # Validate that input is in correct format
            if self.validate_coords(shot_coords, 'firing'):
                # Handle shot
                if defending_board.update_board_with_shot(shot_coords, self):
                    self.check_destroyed_ship(defending_board)
                    break
                if self.owner != 'Computer':
                    print('''
You have already fired at this location, please enter different
co-ordinates''')

    def update_board_with_shot(self, shot_coords, attacking_board):
        '''
        Takes a shot and updates the instance's board_contents to
        show where a shot has landed. Prints out a message
        to user of where shot landed
        '''
        if (self.board_contents[shot_coords] == 'M' or
                self.board_contents[shot_coords] == '@'):
            return False

        if self.board_contents[shot_coords] == '+':

            message = (
                f'\n{attacking_board.owner} fired at {shot_coords} and got a '
                f'direct hit on {self.owner}!'
            )
            print(message)
            self.board_contents[shot_coords] = '@'
            sleep(1)
            return True

        message = (
            f"\n{attacking_board.owner} fired at {shot_coords} and "
            f"missed all of {self.owner}'s ships!"
        )
        print(message)
        sleep(1)
        self.board_contents[shot_coords] = 'M'
        return True

    def check_destroyed_ship(self, def_board):
        '''
        Checks each ship on the defending board to see if it has
        been destroyed. Prints a message to user when a ship
        gets destroyed.
        '''
        for ship in def_board.ships_status:
            # Only check active ships to prevent duplication
            if def_board.ships_status[ship] == 'active':
                coords_to_check = []
                for sect in def_board.ships[ship]:
                    coords_to_check.append(def_board.board_contents[sect])
                if '+' in coords_to_check:
                    continue

                message = (
                    f'{self.owner} destroyed '
                    f"{def_board.owner}'s {ship.capitalize()}!"
                )
                print(message)
                sleep(1.1)
                def_board.ships_status[ship] = 'destroyed'

    def check_for_win(self, defending_board):
        '''
        Checks for a win by seeing if there are any ship sections left
        in the defending_board's board_contents
        '''
        if '+' not in defending_board.board_contents.values():
            print(f'''
{self.owner} has destroyed all of {defending_board.owner}'s ships!''')
            input('\nPress enter key to continue\n')
            return True
        return False

    def reset_variables(self):
        '''
        Resets the Gameboard variables that can change during the game
        '''
        self.board_contents = self.generate_blank_board()
        self.ships = {
            'cruiser': ['', ''], 'submarine': ['', '', ''],
            'destroyer': ['', '', '', '']
        }
        self.ships_status = {
            'cruiser': 'active', 'submarine': 'active',
            'destroyer': 'active'
        }


# Code taken from https://www.101computing.net/python-typing-text-effect/
def typed_print(text):
    '''
    Prints each character individually to the terminal with a 0.02s delay
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.02)


def typed_input(text):
    '''
    Prints each character withn a call to input individually to the terminal
    with a 0.02s delay
    '''
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
    titles.game_title()
    player_response = play_message('first')
    play_or_quit(player_response)
    player_name = get_player_name()
    show_instructions(player_name)
    titles.game_start_text()
    player_board = Gameboard(player_name)
    comp_board = Gameboard('Computer')

    while True:
        player_board.create_ships()
        comp_board.create_ships()
        titles.commence_attack_text()
        player_board.print_both_boards(comp_board)

        while True:
            player_board.fire_shot(comp_board)
            if player_board.check_for_win(comp_board):
                titles.win_lose_text('player')
                break

            comp_board.fire_shot(player_board)
            if comp_board.check_for_win(player_board):
                titles.win_lose_text('computer')
                break
            input('\nPress enter key to continue\n')
            player_board.print_both_boards(comp_board)

        player_response = play_message('rematch')
        play_or_quit(player_response)
        player_board.reset_variables()
        comp_board.reset_variables()


main()
