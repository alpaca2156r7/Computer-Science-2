
'''Name: Katherine Salce
Date: 3/6/2025
Last Edited: 3/4/2025
Description: This code takes in text file containing various columns, and crates a csv file showing the length of the file. 
Bugs: None
Sources: Mr. Campbell
'''
import string                                                    #importing string library
fhand = open('List_for_School.txt','r')                          #input file and reading in data
output = open('Katherine_Salce_Fixed_Length_Converstion', 'w')   #creating variable output, equal to the a new csv file in which the computer will write in information

for line in fhand:                                               #for each line in the file being read in
    id = line[0:4].strip()                                       #variable id, is equal to positions of character inputs and strip extra spaces
    first_name = line[5:19].strip()                              #variable first_name, is equal to positions of character inputs and strip extra spaces
    last_name = line[20:34].strip()                              #variable last_name, is equal to positions of character inputs and strip extra spaces
    grade = line[35:40].strip()                                  #variable grade, is equal to positions of character inputs and strip extra spaces
    g_p_a = line[41:48].strip()                                  #variable g_p_a, is equal to positions of character inputs and strip extra spaces
    birth_date = line[49:60].strip()                             #variable birth_date, is equal to positions of character inputs and strip extra spaces
    gender = line[61:67].strip()                                 #variable gender, is equal to positions of character inputs and strip extra spaces
    class_rank = line[68:76].strip()                             #variable class_rank, is equal to positions of character inputs and strip extra spaces
    attendence_percentage = line[77:86].strip()                  #variable attendence_percentage, is equal to positions of character inputs and strip extra spaces
    honors = line[87:93].strip()                                 #variable honors, is equal to positions of character inputs and strip extra spaces
    sports = line[94:102].strip()                                #variable sports, is equal to positions of character inputs and strip extra spaces
    club_count = line[103:109].strip()                           #variable club_count, is equal to positions of character inputs and strip extra spaces

    output.write(id + "," + first_name + "," + last_name + "," + grade + "," + g_p_a + "," + birth_date + "," + gender + "," + class_rank + "," + attendence_percentage + "," + honors + "," + sports + "," + club_count + "\n")  #write the output of all columns into csv file

output.close()                                                   #after writing output, close file

    


