'''Name: Katherine Salce
Date: 1/29/2025
Description: This code allows the user to play the game hangman. This code keeps track of number of guesses and letters guessed, in order to create displays to match the outcome of the users inputs. 
Bugs: None
Sources:Mr. Campbell, Ms. Marciano, and online website called Geek for Geeks
'''
import random                                                   #importing random function library
easy_word_list = ["wheel","valid", "visit", "train", "yield, voice, story, trust, trend, tired, apple"]                            #list of easy words
medium_word_list = ["change, action, custom, debate, avenue, circle, coffee, behind, belong, bright, bridge"]                      #list of medium words
hard_word_list = ["believe, central, applied, enhance, driving, feature, fitness, genuine, landing, leisure, mineral, mission"]    #list of hard words

hangman_pics = ['''              
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']                                                   #using variable hangman_pics for displaying hangman figures

while True:                                                     #setting up while true loop
    decision_to_play = input("Would you like to play Hangman? ").lower()        #using the variable decision_to_play and setting it equal to asking user to input if they would like to play or not, and making users input lower case
    if decision_to_play == "yes":                               #when decision_to_play is equal to yes 
        print("Let's go!")                                      #print message
    elif decision_to_play=="no":                                #when decision_to_play is equal to no
        break                                                   #end code
    else:                                                       #otherwise
        print("That is not an option!")                         #print message
        continue                                                #go to the top of loop and start again

    user_level_choice = input("What level would you like to choose? Easy(5 letters), Medium(6 letters), Hard(7 letters): ").lower() #using the variable user_level_choice and setting it equal to asking user what level they would like to choose, and making users input lower case 
    
    if user_level_choice == "easy":                             #when user_level_choice is equal to easy
        selected_word = random.choice(easy_word_list)           #using variable selected_word and setting it equal to random word choice from the list easy_word_list
    elif user_level_choice == "medium":                         #when user_level_choice is equal to medium
        selected_word = random.choice(medium_word_list)         #using variable selected_word and setting it equal to random word choice from the list medium_word_list
    else:                                                       #otherwise
        selected_word = random.choice(hard_word_list)           #using variable sleected_word and setting it equal to random word choice from the list hard_word_list

    selected_word = ""                                          #making selected word a string
    display = []                                                #setting up display variable
    count = 0                                                   #making original number of guesses equal to 0
    
    while count < len(selected_word):                           #while the number of gallows is less than the length of the selected word
        display.append("_")                                     #displaying the same number of underlines as characters in the randomly selected_word
        count += 1                                              #counting each character as one more underline
    
    print(hangman_pics[0])                                      #printing the first hangman picture 
    print(" ".join(display))                                    #printing display
    guesses = 0                                                 #setting original amount of guesses equal to 0
    available = list("abcdefghijklmnopqrstuvwxyz")              #setting variable available equal to a list containing the alphabet
    print(f'Available letters: {", ".join(available)}')         #printing list of all availbale characters
    

    while guesses < 6 and "_" in display:                       #telling code to run 6 times, giving user 6 guesses
        user_letter_input = input("\nEnter a letter: ").lower() #setting up prompt after every guess to allow user to enter a new letter

        if user_letter_input not in available:                  #when the letter inputted by the user is not in the available characters list
            print("Please enter an available letter!")          #print message
            continue                                            #go to the top of the loop and start again

        if user_letter_input in selected_word:                  #when a users inputted letter is in the randomly selected word
            hidden_word = list(selected_word)                   #hidden word is going to be equal to list of letters in selected word

            for i in range(len(hidden_word)):                   #as user inputted letter is seen in randomly selected word
                if hidden_word[i] == user_letter_input:         #when the hidden word contains the user inputted letter
                    display[i] = user_letter_input              #displaying correct inputted letter in appropriate position in selected word 
        else:                                                   #otherwise
            print("That letter is not here!")                   #print message
            guesses += 1                                        #setting variable guesses equal to plus one, every wrong letter input takes away guess

        available.remove(user_letter_input)                     #removing letters already guessed by user
        print(hangman_pics[guesses])                            #print hangman picture after each guess and add on to picutre after each wrong letter
        print(" ".join(display))                                #printing display
        print(f"You have {6-guesses} left")                     #printing number of guesses left
        print(f'Available letters: {", ".join(available)}')     #printing list of all available characters

    if guesses >= 6:                                            #when the number of guesses are greater than or equal to 6
        print("You lost this round! The word was", selected_word) #printing phrase and selected word
    else:                                                       #otherwise
        print("You got it! The word was", selected_word)        #printing phrase and selected word
    