import os


class Headings:
    def game_title():
        '''
        Prints 'Battleships' title to terminal
        '''
        print('''
  ____       _______ _______ _      ______    _____ _    _ _____ _____   _____
 |  _ \   /\|__   __|__   __| |    |  ____|  / ____| |  | |_   _|  __ \ / ____|
 | |_) | /  \  | |     | |  | |    | |__    | (___ | |__| | | | | |__) | (___
 |  _ < / /\ \ | |     | |  | |    |  __|    \___ \|  __  | | | |  ___/ \___ \\
 | |_) / ____ \| |     | |  | |____| |____   ____) | |  | |_| |_| |     ____) |
 |____/_/    \_\_|     |_|  |______|______| |_____/|_|  |_|_____|_|    |_____/
''')

    def rules():
        '''
        Prints 'Rules' title and rules to terminal
        '''
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
You will be given three ships to place on your board, and your opponenet
will do the same with their board. The ships sizes are: 1x2 (Cruiser),
1x3 (Submarine) and 1x4 (Destroyer).

The objective is to sink your opponent's ships by supplying the
co-ordinates of where you think they have placed their ships. The first
player to sink all the opponent's ships is the winner.

To keep track of your shots, you will be provided with a 'guess' board.
The symbols on the board are as follows:
~ = An untouched section of a board
+ = An undamaged section of a ship
@ = A section of a ship which has been hit
M = A shot which missed''')

        input('\nPress enter key to continue\n')
        return

    def game_start_text():
        '''
        Prints 'Game Start' title to terminal
        '''
        clear_console()
        print('''
   _____          __  __ ______    _____ _______       _____ _______
  / ____|   /\   |  \/  |  ____|  / ____|__   __|/\   |  __ \__   __|
 | |  __   /  \  | \  / | |__    | (___    | |  /  \  | |__) | | |
 | | |_ | / /\ \ | |\/| |  __|    \___ \   | | / /\ \ |  _  /  | |
 | |__| |/ ____ \| |  | | |____   ____) |  | |/ ____ \| | \ \  | |
  \_____/_/    \_\_|  |_|______| |_____/   |_/_/    \_\_|  \_\ |_|
''')

        input('\nPress enter key to continue\n')
        return

    def commence_attack_text():
        '''
        Prints 'Commence Attack' title to terminal
        '''
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
        input('\nPress enter key to continue\n')
        clear_console()
        return

    def win_lose_text(winner):
        '''
        Prints 'You Win' or 'You Lose' title to terminal
        '''
        clear_console()
        if winner == 'player':
            print('''
 __     ______  _    _  __          _______ _   _
 \ \   / / __ \| |  | | \ \        / /_   _| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |
    |_|  \____/ \____/      \/  \/   |_____|_| \_|
''')

        if winner == 'computer':
            print('''
 __     ______  _    _   _      ____   _____ ______
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
    | | | |__| | |__| | | |___| |__| |____) | |____ 
    |_|  \____/ \____/  |______\____/|_____/|______|
''')
        input('\nPress enter key to continue\n')
        clear_console()
        return


# Code taken from https://www.delftstack.com/howto/python/python-clear-console/
def clear_console():
    '''
    Clears the terminal
    '''
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
# End of code taken from delftstack.com