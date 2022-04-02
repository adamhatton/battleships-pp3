import sys

print(
    '''
  ____       _______ _______ _      ______    _____ _    _ _____ _____   _____ 
 |  _ \   /\|__   __|__   __| |    |  ____|  / ____| |  | |_   _|  __ \ / ____|
 | |_) | /  \  | |     | |  | |    | |__    | (___ | |__| | | | | |__) | (___  
 |  _ < / /\ \ | |     | |  | |    |  __|    \___ \|  __  | | | |  ___/ \___ \ 
 | |_) / ____ \| |     | |  | |____| |____   ____) | |  | |_| |_| |     ____) |
 |____/_/    \_\_|     |_|  |______|______| |_____/|_|  |_|_____|_|    |_____/ 
    '''
)

def welcome_message():
    '''
    Prints welcome message to user, asks if they want to play a game and
    collects user input
    '''  
    while True:
        print('Would you like to play a game?\n')
        print('[y] = yes, [n] = no\n')

        answer = input('\n')

        if validate_input(answer):
            print('yay')
            break

    return answer


def validate_input(input):
    try:
        input.lower()
    
    except AttributeError:
        print('Invalid input, please try again')
        return False
    
    return True



def main():
    welcome_message()

main()