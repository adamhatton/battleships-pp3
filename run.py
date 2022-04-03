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

    return player_answer


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


def main():
    welcome_message()
    print('code got to main()')

main()