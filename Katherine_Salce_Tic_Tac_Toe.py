
import random                                                                                           #importing random library

def printBox(box):                                                                                      #defining the function printbox, taking in the parameter box
    for i in range (len(box)):                                                                          #
        for j in range (len(box[i])):                                                                   #
            print(box[i][j], end=' ')                                                                   #
        print("")                                                                                       #
            
                
def CheckWinner(choice, box):                                                                           #defining function CheckWinner taking in parameters choice and box
    game = "go"                                                                                         #when game is equal to "go" (in the process of being played)
    if box[0][0] == choice and box[0][1] == choice and box[0][2] == choice:                             #check 3 top horizontal spots for the same letter
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the top spots match
        game = "stop"                                                                                   #when game is equal to "stop" (the game is ended since winner was already declared)
        
    elif box[1][0] == choice and box[1][1] == choice and box[1][2] == choice:                           #check 3 middle horizontal spots for the same letter
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the middle spots match
        game = "stop"                                                                                   #when game is equal to "stop" (the game is ended since winner was already declared)
        
    elif box[2][0] == choice and box[2][1] == choice and box[2][2] == choice:                           #check 3 bottom horizontal spots for the same letter
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the bottom spots match
        game = "stop"                                                                                   #when the game is equal to "stop" (the game is ended since winner was already declared)
        
    elif box[0][0] == choice and box[1][1] == choice and box[2][2] == choice:                           #check 3 diagonal spots from top left to bottom right for the same letter
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the diagonal spots match
        game = "stop"                                                                                   #when the game is equal to "stop" (the game is ended since winner was already declared)
        
    elif box[0][2] == choice and box[1][1] == choice and box[2][0] == choice:                           #check 3 diagonal spots from top right to bottom left for the same letter                                               
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the diagonal spots match
        game = "stop"                                                                                   #when the game is equal to "stop" (the game is ended since winner was already declared)
        
    elif box[0][0] == choice and box[1][0] == choice and box[2][0] == choice:                           #check 3 spots in first column (vertically) for the same letter
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the spots in the first column match
        game = "stop"                                                                                   #when the game is equal to "stop" (the game is ended since winner was already declared)
               
    elif box[0][1] == choice and box[1][1] == choice and box[2][1] == choice:                           #check 3 spots in second column (vertically) for the same letter
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the spots in the second column match
        game = "stop"                                                                                   #when the game is equal to "stop" (the game is ended since winner was already declared)
        
    elif box[0][2] == choice and box[1][2] == choice and box[2][2] == choice:                           #check 3 spots in third column (vertically) for the same letter 
        print(choice + " is winner!")                                                                   #printing winner's letter and message saying "you win" if the spots in the third column match
        game = "stop"                                                                                   #when the game is equal to "stop" (the game is ended since winner was already declared)
    return game                                                                                         #returning the results from the game   
def checkSpot(box,current_player):                                                                      #defining the function checkSpot taking in parameters box and current_player
    user_player_spot_choice = ""                                                                        #returning user_player_spot_choice as a string
    while True:                                                                                         #prompting loop, usign conditional while the statement is true
        printBox(box)                                                                                   #
        if current_player == 'X':                                                                       #if the current_player equals X
            user_player_spot_choice = input ("What spot would you like to choose?")                     #asking user to input a spot choice and setting it equal to user_player_spot_choice
        
        else:                                                                                           #otherwise
             user_player_spot_choice = str(random.randint(1,9))                                         #computer selects random integer between 1 and 9, turns the output into a string, and makes the random string(number) equal to user_player_spot_choice 

        if user_player_spot_choice == "1" and box[0][0] == 1:                                           #if current_player choses the number 1 check to see if position is equal to 1
            box[0][0] = current_player                                                                  #current_player letter entered into position to declare possesion
            break                                                                                       #ending code

        elif user_player_spot_choice == "2" and box[0][1] == 2:                                         #if current_player choses the number 2 check to see if position is equal to 2
           box[0][1] = current_player                                                                   #current_player letter entered into position to declare possesion
           break                                                                                        #ending code

        elif user_player_spot_choice == "3" and box[0][2] == 3:                                         #if current_player choses the number 3 check to see if position is equal to 3
            box[0][2] = current_player                                                                  #current_player letter entered into position to declare possesion
            break                                                                                       #ending code

        elif user_player_spot_choice == "4" and box[1][0] == 4:                                         #if current_player choses the number 4 check to see if position is equal to 4
            box[1][0] = current_player                                                                  #current_player letter entered into position to declare possesion
            break                                                                                       #ending code                                                   
        
        elif user_player_spot_choice == "5" and box[1][1] == 5:                                         #if current_player choses the number 5 check to see if position is equal to 5
            box[1][1] = current_player                                                                  #current_player letter entered into position to declare possesion
            break                                                                                       #ending code

        elif user_player_spot_choice == "6" and box[1][2] == 6:                                         #if current_player choses the number 6 check to see if position is equal to 6
            box[1][2] = current_player                                                                  #current_player letter entered into position to declare possesion
            break                                                                                       #ending code

        elif user_player_spot_choice == "7" and box[2][0] == 7:                                         #if current_player choses the number 7 check to see if position is equal to 7 
           box[2][0] = current_player                                                                   #current_player letter entered into position to declare possesion
           break                                                                                        #ending code

        elif user_player_spot_choice == "8" and box[2][1] == 8:                                         #if current_player choses the number 8 check to see if position is equal to 8 
           box[2][1] = current_player                                                                   #current_player letter entered into position to declare possesion
           break                                                                                        #ending code

        elif user_player_spot_choice == "9" and box[2][2] == 9:                                         #if current_player choses the number 9 check to see if position is equal to 9
            box[2][2] = current_player                                                                  #current_player letter entered into position to declare possesion
            break                                                                                       #ending code
         
        else:                                                                                           #otherwise
            print("Invalid Spot either not between 1-9 or spot already taken!")                         #printing messege 
            continue                                                                                    #going back to the top of while true fucntion (looping)
            #increment counter by 1
            #check winner


def main():                                                                                             #defining the function main
    box = [[1,2,3],                                                                                     #setting up box format
        [4,5,6],                                                                                        #setting up box format
        [7,8,9]]                                                                                        #setting up box format
    game_loop = True                                                                                    #game_loop is equal to true
    user_score = 0                                                                                      #user score starts at 0
    bot_score = 0                                                                                       #bot score starts at 0
    count = 0                                                                                           #setting count equal to 0
    
    while game_loop:                                                                                    #while completing the function game_loop
        user_start = input("Would you like to play Tic-Tac-Toe?").lower()                               #asking for user to input whether or not they want to play Tic-Tac-Toe
        if user_start == "yes":                                                                         #if user inputs, yes
                print('ok ...here we go')                                                               #print message                                                           
        else:                                                                                           #otherwise
                print("bye")                                                                            #print message
                exit()                                                                                  #stop rest of code

        
        user_player_number = input("How many players: Type 1:")                                         #asking for user input as to how many players
        bot_player_assignment = ""                                                                      #adding computer as player
        user_player_assignment = ""                                                                     #adding user as player
        status = "go"                                                                                   #status is set to go (game will begin being played)                                               

        if user_player_number == "1":                                                                   #if the user enters the number 1
            user_player_assignment = "X"                                                                #user is assigned the letter X
            print ("You are player X")                                                                  #print message
            bot_player_assignment = "O"                                                                 #computer is assigned the letter O
            print ("Bot is player O")                                                                   #print message                                                           

                                                                
        turn = random.choice(['X','O'])                                                                 #randomly choosing who goes first

        while count < 9:                                                                                #while the number of position entries (or turns) is less than 9
            
            if turn == "O":                                                                             #if turn is equal to player O
                current_player = "O"                                                                    #variable current_player is equal to O
                print("O's Turn!")                                                                      #print messege
                checkSpot(box, current_player)                                                          #calling function checkSpot taking in parameteres box and current_player
                turn = "X"                                                                              #second turn equal to player X
                current_player = user_player_assignment                                                 #setting current_player to user_player_assignment 
                status = CheckWinner(current_player, box)                                               #checking for winner using parameters current_player and box to assess status of game
                if status == "stop":                                                                    #if user inputs, stop
                    print("Game Over!")                                                                 #print messege
                    break                                                                               #ending code
                count = +1                                                                              #after each move add 1 to count
            
            
            elif turn == "X":                                                                           #if turn is equal to player X
                current_player ="X"                                                                     #variable current_player is equal to X
                print("X's Turn!")                                                                      #print messege
                
                checkSpot(box, current_player)                                                          #calling function checkSpot taking in parameters box and current_player
                count = +1                                                                              #after each game add 1 to count
                turn = "O"                                                                              #second turn equal to player O
                current_player = user_player_assignment                                                 #setting current_player to user_player_assignment
                status = CheckWinner(current_player, box)                                               #checking for winner using parameters current_player and box to assess status of game
                if status == "stop":
                    print("Game Over!")
                    break
            
                


            if status == "stop":                                                    #if status is equal to stop (when game has ended)
                if user_score > bot_score:                                          #when the user's score is higher than the bot's score
                    print ("You WON! Great job.")                                   #print the message 
                elif user_score < bot_score:                                        #when the user's score is smaller than the bot's score
                    print ("You lost. Sorry.")                                      #print the message 
                elif user_score == bot_score:                                       #when user's score and bot's score are equal
                    print ("You tied.")                                             #print the message 

                    user_number_of_inputs = 0                                       #user's score starts at zero
                    bot_number_of_inputs = 0                                        #bot's score starts at zero
    

if __name__ == "__main__":                                                          #

    main()                                                                          #run the main function
