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


def validate_input(input):
    '''
    Validates user input and returns True if it is valid or False if it is not
    '''
    try:
        if input == 'y' or input == 'n':
            return True
        else:
            raise Exception
    except Exception:
        print("Input must be 'y' or 'n', please try again\n")
        return False
    return True


def play_or_quit(answer):
    if answer:
        pass
    else:
        print(
            '''Closing game. If you change your mind, press the 'Run Program'
button above to restart the game''')
        sys.exit()


def main():
    player_response = welcome_message()
    play_or_quit(player_response)

main()