'''
Name: Katherine Salce
Date: 2/31/2025
Description: This code allows user to enter their full name, and carry out various functions that alter the characters in various ways.
Bugs: None
Last Accessed:2/24/2025
Sources:  https://stackoverflow.com/questions/62350365/how-to-count-the-total-number-of-vowels-in-a-string
'''
import random                               #calling random library
def user_name(name):                        #creating a function called user_name, taking in the parameter name
    print("Your name is:", name)            #print message and users inputted name
def reverse_name(name):                     #creating a function called reverse_name, taking in the parameter name
    print(name[::-1])                       #users name in reverse
    return name[::-1]                       #store the variable, reversed name
def count_vowels(name):                     #creating a function called count_vowels, taking in the parameter name 
    count = 0                               #setting orginal variable, count, equal to zero
    vowels = list('aeiou')                  #setting up variable, vowels, and setting it equal to a list of vowels

    for n in name:                          #if letter in name
        if lowercase(n) in vowels:          #if lowercase letter in name is part of vowel list
            count += 1                      #add one to count every time vowel appears in the name entered
    return count                            #store the variable count, which is equal to the number of times vowels appear
def consonant_frequency(name):              #creating a function called consonant_frequency, taking in the parameter name
    count = 0                               #setting original variable, count, equal ot zero
    consonants = list('bcdfghjklmnpqrstvwxyz') #setting up variable consonants, and setting it equal to a list of consonants

    for n in name:                          #if letter in name
        if lowercase(n) in consonants:      #if lowercase letter in name is part of consonant list
            count += 1                      #add one to count every time consonant appears in the name entered
    return count                            #store the variable count, which is equal to the number of times each consonant appear
def subtotal(name):                         # creating a function called subtotal, taking in the parameter name
    total = {}                              #creating variable named total, and setting it equal to the sum of name
 
    for c in list('bcdfghjklmnpqrstvwxyz'): #iterating through consonants
        total[c] = 0                        #total count of original dictionary
    
    for n in name:                          #for characters in name
        if lowercase(n) in total.keys():    #turn all characters lowercase
            total[lowercase(n)] += 1        #find consonants and add one every time consonant shows up
    return total                            #returning total number of consonants in users inputted name
def contains_title(name):                   #creating a function called contains_title, taking in the parameter name
    names = name.split(" ")                 #creating variable named names, and setting it equal to the variable name which is being split based on spaces in between
    titles = ['dr.', 'doctor', 'reverend', 'sr.', 'senior', 
    'prince', 'king', 'professor','private', 'specialist', 'corporal', 'sergeant', 'captain', 
    'major', 'colonel']           #creating a variable named, titles, and setting it equal to a list of job titles typically seen

    for name in names:                      #for name in names
        if lowercase(name) in titles:       #if name in titles is lowercase
            return True                     #store the answer true
    return False                            #store the answer false
def remove_title(name):                     #creating function named remove_title, taking in the parameter name
    names = name.split(" ")                 #creating variable named names, and setting it equal to splitting the name and taking in the parameter of an empty string
    titles = ['dr.', 'doctor', 'reverend', 'sr.', 'senior', 
    'prince', 'king', 'professor','private', 'specialist', 'corporal', 'sergeant', 'captain', 
    'major', 'colonel']            #creating a variable named, titles, and setting it equal to a list of job titles typically seen

    for name in names:                      #for name in names
        if lowercase(name) in titles:       #if name in titles is lowercase
            names.remove(name)              #removing name from the variable names
    return names                            #store the variable named
def get_first_name(name):                   #creating a function named get_first_name, taking in the parameter name
    return remove_title(name)[0]            #store name(removed titles) in between the parameters
def get_last_name(name):                    #creating a function named get_last_name, taking in the parameter name
    
    return remove_title(name)[-1]           #store name(removed titles) in between parameters
def get_middle_names(name):                 #creating a function named get_middle_names, taking in the parameter name
    return ' '.join(remove_title(name)[1:-1])  #store empty string joining name(removed titles) in between the parameters
def contains_hyphen(name):                     #creating a function named contains_hyphen, taking in the parameter name
    return '-' in get_last_name(name)          #store hyphen in the function get_last_name taking in the parameter name
def lowercase(name):                           #creating a function named lowercase, taking in the parameter name
    lower = ''                                 #creating a variable lower, and setting it equal to an empty string
    
    for char in name:                          #for character in name
        if 'A' <= char <= 'Z':                 #if the characters are in between uppercase a and z
            lower += chr(ord(char) + 32)       #creating variable named upper, adding and setting it equal to character, it's order in the alphabet lower dictionary and returning the new character
        else:                                  #otherwise
            lower += char                      #creating a variable lower, adding and setting it equal to characters
    return lower                               #store the variable lower
def uppercase(name):                           #creating function named uppercase, taking in the parameter name
    upper = ''                                 #creating a variable upper, and setting it equal to an empty string 

    for char in name:                          #for characters in name
        if 'a' <= char <= 'z':                 #if the characters are in between lowercase a and z 
            upper += chr(ord(char) - 32)       #creating variable named upper, adding and setting it equal to character, it's order in the alphabet upper dictionary and returning the new character 
        else:                                  #otherwise
            upper += char                      #creating a variable upper, adding and setting it equal to characters
    return upper                               #store the variable upper
def modify_array(name):                        #creating function named modify_array, taking in the parameter name
    name_split = list(name)                    #creating variable named name_split, and setting it equal to a list function taking in the parameter name

    random.shuffle(name_split)                 #calling random shuffle function taking in the parameter name_split

    name = ''.join(name_split)                 #creating the variable name, and setting it equal to an empty string joining the parameter name_split
    
    print(name)                                #print the parameter name

    return name                                #store the variable name

def palindrome(name):                         #defining the function palindrome, taking in the parameter name
    return name == reverse_name(name)         #store name, that is the same as the function reverse_name taking in the parameter name
def make_initials(name):                      #defining the function make-initials, taking in the parameter name
    names = remove_title(name)                #creating variable named names, and setting it equal ot the function remove title taking in the parameter name 
    initial = ''                              #creating variable named initial, and setting it equal to an empty string

    for name in names:                        #for each name in names
        initial = initial +  name[0]          #creating variable named initial and setting it plus and equal to the first item in name list
    
    return initial                            #store the variable initials, which is equal to the first letter in your first, middle and last name

def main():                                   #creating a function called main, taking in no explicit parameters
    name = input("Please enter your full name! ")   #creating a variable named user_name and setting it equal to users input to the prompt "Please enter your first name"
    print('''

    1.Reverse Name, 
    2.Count Vowels, 
    3.Consonant Frequency, 
    4.Consonant Subtotal
    5.Get First Name, 
    6.Get Last Name, 
    7.Get Middle Names, 
    8.Check hyphen
    9.Convert Whole Name to Lowercase, 
    10.Convert Whole Named to Uppercase,
    11.Modify Array (mix up letters),
    12.Palindrome,
    13.Make Initials, 
    14.Check Title
    ''')                                                     #creating variable named function_use, and setting it equal to users input to the following prompt
    while True:                                              #creating loop 
        function_use = input('What do you want to do? ')        #creating variable named function_use, and setting it equal to users input to the prompt
        if function_use == "1":                                 #if user inputs the number one
            reverse_name(name)                                  #print reversed name
        elif function_use == "2":                               #or if user inputs the number two
            print(count_vowels(name))                           #print vowel count in name
        elif function_use == "3":                               #or if user inputs the number three
            print(consonant_frequency(name))                    #print count for each individual consonant in name
        elif function_use == "4":                               #or if user inputs the number four
            total = subtotal(name)                              #creating variable named total and setting it equal to subtotal function taking in the parameter name
            print(total)                                        #print total count for all consonant in name

            for key in total.keys():                            #for jeys in the total number of keys
                if total[key] > 0:                              #total amount of keys has to be grater than zero
                    print(f'{key}: {total[key]}')               #printing key and value or the key
        elif function_use == "5":                               #or if user inputs the number five
            print(get_first_name(name))                         #print first name
        elif function_use == "6":                               #or if user inputs the number six
            print(get_last_name(name))                          #print last name
        elif function_use == "7":                               #or if user inputs the number seven
            print(get_middle_names(name))                       #print middle name
        elif function_use == "8":                               #or if user inputs the number eight
            print(contains_hyphen(name))                        #return true or false based on if there is a hyphen present
        elif function_use == "9":                               #or if user inputs the number nine
            print(lowercase(name))                              #print lowercase
        elif function_use == "10":                              #or if user inputs the number 10
            print(uppercase(name))                              #print uppercase
        elif function_use == "11":                              #or if user inputs the number eleven
            print(modify_array(name))                           #print modified array
        elif function_use == "12":                              #or if user inputs the number twelve
            print(palindrome(name))                             #print palindrome
        elif function_use == "13":                              #or if user inputs the number thirteen
            print(make_initials(name))                          #print initials
        elif function_use == "14":                              #or if user inputs the number fourteen
            print(contains_title(name))                         #print title (if available)
        else:                                                   #otherwise
            print("That is not an option!")                     #print message
            continue                                            #go back to the start of the loop
            
   
main()                                                          #calling main function
