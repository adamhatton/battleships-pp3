# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    print('Would you like to play a game?\n')
    print('[y] = yes, [n] = no')

welcome_message()