
'''Name: Katherine Salce
Date: 
Last Edited: 3/4/2025
Description: 
Bugs: None
Sources: Mr. Campbell
'''
import string
fhand = open('List_for_School.txt','r') #input file
output = open('Katherine_Salce_Fixed_Length_Converstion', 'w')

for line in fhand:
    id = line[0:4].strip()
    first_name = line[5:19].strip()
    last_name = line[20:34].strip()
    grade = line[35:40].strip()
    g_p_a = line[41:48].strip()
    birth_date = line[49:60].strip()
    gender = line[61:67].strip()
    class_rank = line[68:76].strip()
    attendence_percentage = line[77:86].strip()
    honors = line[87:93].strip()
    sports = line[94:102].strip()
    club_count = line[103:109].strip()

    output.write(id + "," + first_name + "," + last_name + "," + grade + "," + g_p_a + "," + birth_date + "," + gender + "," + class_rank + "," + attendence_percentage + "," + honors + "," + sports + "," + club_count + "\n")

output.close()

    


