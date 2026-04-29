#This program will create a number guessing game
#users will guess a random number until they get the correct number
#then ask users if they want to play again and so on

import random

#create a global constant
HISTORY_FILE = 'history.txt'
#create two global variables
game_history_names = []
game_history_guesses = []


# create a main function to contral this program
def main():
    display_scores()
    get_player_name()
    repeat_game()
    store_name(game_history_names,game_history_guesses)

    
# display the header and line
# read the history of player 
def display_scores():
    print(f'Winner Name\t\tGuesses')
    print(f'-------------------------------')
    #call read_history() function
    read_history()


def read_history():
    try:
        #open the file and read data
        infile= open(HISTORY_FILE, "r")
        # the error of program could not find the file
    except IOError:
        print("Error trying to access history.txt")
    else:
        #read player's name
        player_name = infile.readline()
        while player_name != "":
            player_name = player_name.rstrip("\n")  
            game_history_names.append(player_name)

            #read the values of history
            score = infile.readline()
            score = score.rstrip("\n")
            #data of score
            game_history_guesses.append(score)

            #read another player's name
            player_name = infile.readline()
        #create a value for number of line    
        count = 0
        #set the first player as a winner first
        min_score = game_history_guesses[0]
        min_name = game_history_names[0]
        #create a for loop to get the data of former player
        for row in range(0,len(game_history_guesses)):
            count += 1
            #if next player's score less than last player's score
            #set the next player as a winner
            if game_history_guesses[row] < min_score:
                min_score = game_history_guesses[row]
                min_name = game_history_names[row]

        #output the data of winner       
        print(f'{min_name:<15}\t{min_score:>15}')  

#create a function of getting user's name
def get_player_name():
    #input the name
    name = input('Please enter your name: ')
    #append the name to the Global variable list of name
    game_history_names.append(name)
    #return the user_name
    return name

#create a function of play the game and repeat the game
def repeat_game():
    #create a list for picking up the least times as a score of user
    x = []
    again = 0
    #if player want to play again
    play_again = 'y' or 'Y'
    while again != 1:
        if play_again =='y' or play_again =='Y':
            #the time for asking user a number
            time = 1
            #create a random number for user and range is 1 to 100
            number_range =list(range(1,101))
            a = random.choice(number_range)
            print(f'test: --{a}--') ########## test

            #ask user what's the number
            user_number = int(input(f'#{time} Guess an integer number between 1 and 100: '))
            #if the user's number incorrect
            while user_number != a:
                #if user's number less than random number
                if user_number < a:
                    #output guess is too low
                    print('Your guess is too low.')
                #if user's number higher than random number
                elif user_number > a:
                    #output guess is too high
                    print('Your guess is too high.')

                # continuing asking the number
                user_number = int(input(f'#{time+1} Gusee an integer number between 1 and 100: '))
                #time +1
                time += 1
            if user_number == a:
                print(f'Congratulations - You are correct!')
                print(f'Number of guesses: {time}')
            #write all of times which user guesses
            x.append(time)
            play_again = input('Would you like to play again(y/n)?: ')

        #ask user if they want to play again    
        elif play_again == 'n' or play_again == 'N':
            again = 1
        else:
            print('Not a vaild entry (Y/y or N/n)')
            play_again = input('Would you like to play again (y/n)?: ')
            
    #pick up the least time as a score 
    value = int(min(x))
    #write this score to the Global variable list
    game_history_guesses.append(value)
  
                  
#create a function to store user name and score
def store_name(game_history_names,game_history_guesses):
    #open the file of history
    with open(f'{HISTORY_FILE}','w') as infile: 
        #get two Gloabal variable lists
        for p in range(0,len(game_history_names)):
            # combine the names and their score
            infor = game_history_names[p]+'\n'+ str(game_history_guesses[p])+'\n'
            #write the data to the file of history
            infile.write(infor)

#call the main function
if __name__=='__main__':
    main()
