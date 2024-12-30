"""Name: Katherine Salce
Date: 11/1/2024
Last Edited: 11/1/2024
Description: Taking in a file and counting the number of times each word is said.
Bugs: None
Sources: Python For Everbody - Exploring Data in Python 3"""
import string                                                                                                     #importing string function from function library
count = 0                                                                                                         #setting orginal count equal to zero
fhand = open('kamala_new.txt')                                                                                    #making an fhand variable that opens a text file 
counts = dict()                                                                                                   #counting each time word in dictionary is used

bad_words = ['as','to','an','it','a','is','the','but','on','of','and','when','are','that','in', 'this', 'would','have', 'be','has','their','not','know','was','who','with']  #variable bad words takes out words that are not useful to the narrative of the story



for line in fhand:                                                                                                #reading in lines from file
   
    line = line.translate(str.maketrans('', '', string.punctuation))                                              #making words in line punctuated
    line = line.lower()                                                                                           #making words in line lowercase
    words = line.split(" ")                                                                                       #splitting lines into words and making them into strings
    for word in words:                                                                                            #creating function for word in words
        if word in bad_words:                                                                                     #if string matches word in bad_words
            continue                                                                                              #skip over
        else:                                                                                                     #otherwise
            if word not in counts:                                                                                #if string doesn't match word in bad_words
                counts[word] = 1                                                                                  #adding word to final output
            else:                                                                                                 #otherwise
                counts[word] += 1                                                                                 #each time word shows up, add one to string count
counts.pop("\n")                                                                                                  #getting rid of new lines


print(counts)                                                                                                     #print counts for each string

       
election_file = open ('Katherine_Salce_Election_Word_Count_Harris.csv', 'w')                                      #making variable called election_file and setting it equal to open which allows file to access data from fiel and write into alternative file


for key, val in counts.items():                                                                                #for final output count number of tiems string was used
    if val > 10:                                                                                               #if number of times string was used, is greater than 10
        election_file.write(key + "," + str(val) + "\n")                                                       #write out strings and number of times each string is used in file, after each charatcer enter new line 
       
       



