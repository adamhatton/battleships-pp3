import sys

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
    def __init__(self, owner):
        self.rows = 6
        self.cols = 6
        self.row_coordinates_key = ('A', 'B', 'C', 'D', 'E', 'F')
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
                board_grid.update({f'{self.row_coordinates_key[row]},{col}': '~'})

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
            row_to_print = f'{self.row_coordinates_key[row]}' + '| '
            for col in range(self.cols):
                row_to_print += self.board_contents[f'{self.row_coordinates_key[row]},{col}'] + ' | '
            print(row_to_print)

        # Adds border to bottom
        print(' -' * 13)

    def place_ships(self):
        for ship in self.ships:
            while True:
                print(f'Where would you like to place {ship}?')
                print('Enter the starting co-ordinate followed by V for vertical placement or H for horizontal placement, e.g. A2H or C4V')
                ship_placement = input().lower()
                if validate_ship_input(ship_placement):
                    break
            print(ship)

def validate_ship_input(user_input):
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
        print('Unknown error with your input, please try again')
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
    player_board.place_ships()
    print('code got back to main()')

main()
