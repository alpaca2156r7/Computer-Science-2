

"""Name: Katherine Salce
Date: 10/30/2024
Description:  This program takes in the parameters of height, length, thickness, zip from and zip to. The computer then outputs the zone difference, postage type and total cost.
Bugs: None
Sources: Mr. Campbell """
def get_postage_type(length, height, thickness):                            #defining new function named 'get_postage_type'                                                        #
    if 3.5<height<6 and 3.5<length<4.25 and .007<thickness<.016:         #if parameters are met
        return "Regular Post Card"                                          #returning the variable Regular Post Card to user
    elif 6<height<11.5 and 4.25<length<6 and.007<thickness<.015:            #if parameters are met
        return "Large Post Card"                                             #returning the variable Large Post Card to user
    elif 5<height<11.5 and 3.5<length<6.125 and .016<thickness<.25:         #if parameters are met
        return "Envelope"                                                    #returning the variable Envelope to user
    elif 11<height<18 and 6.125<length<24 and .25<thickness<.5:             #if parameters are met
        return "Large Envelope"                                              #returning the variable Large Envelope to user
    elif 11<height<18 + length*2>84 and .5<thickness:                           #if parameters are met
        return "Package"                                                     #returning the variable Package to user
    elif 84<height*2 + length*2>130 and .5<thickness:                       #if parameters are met
        return "Large Package"                                               #returning the variable Large Package to user
    else:                                                                   #otherwise
        return "Unmailable"                                                  #returning the variable Unmailable to user and ending code 
                                        
def main():                                                                 #defining main function
    answers = input("Please Print length (in inches), height (in inches), thickness (in inches) of Package! As well as from and to zip codes")    #variable answer is equal to users input to prompt given by computer

    dimensions = answers.split(",")                                         #variable 'dimensions' takes users input and splits them into indexes within a list 

    height = float(dimensions[0])                                      #defining the variable 'height' which is part of the dimension variable and added to list as index 0
    length = float(dimensions[1])                                      #defining the variable 'length' which is part of the dimension variable and added to list as index 1
    thickness = float(dimensions[2])                                  #defining the variable 'thickness' which is part of dimension variable and added to list as index 2
    zip1 = int(dimensions[3])                                       #defining the variable 'zip1' which is part of dimension variable and added to list as index 3
    zip2 = int(dimensions[4])                                      #defining the variable 'zip2' which is part of dimension variable and added to list as index 4

    
    difference = abs(get_zone_skip(zip2) - get_zone_skip(zip1))      #defining the variable 'difference' that takes in parametrs zip2 and zip1 

    mail_type = get_postage_type(height,length,thickness)           #defining the variable 'mail_type' which is equal to the function get_postage_type taking in the parameters height, length, thickness

    end_cost =  total_cost_of_shipping(mail_type,difference)        #defining the variable 'end_cost' which is equal to the funtion total_cost_of_shipping taking in the parameters mail_type and difference 

    print(difference)                                               #printing the difference of zip codes
    print (mail_type)                                               #printing the mail type calculated by height, length and thickness inputed
    print (end_cost)                                                #printing the end cost taking returned difference and mail_type
    

def get_zone_skip(zip):                                     #defining a new function named 'get_zone_skip' that takes in parameter zip
                                                            
    if zip>1 and zip<6999:                                 #if the parameters for zip1 and zip2 are met
        return 1                                            #returning the variable zone 1 to user
    elif zip>7000 and zip<19999:                             #if the parameters for zip1 and zip2 are met
        return 2                                           #returning the variable zone 2 to user
    elif zip>20000 and zip<35999:                             #if the parameters for zip1 and zip2 are met
        return 3                                            #returning the variable zone 3 to user
    elif zip>36000 and zip<62999:                            #if the parameters for zip1 and zip2 are met
        return 4                                            #returning the variable zone 4 to user
    elif zip>63000 and zip<84999:                            #if the parameters for zip1 and zip2 are met
        return 5                                           #returning the variable zone 5 to user
    elif zip>85000 and zip<99999:                            #if the parameter 
        return 6                                            #returning the variable zone 6 to user
                                             

                                     #returning the difference of zip2 and zip1

def total_cost_of_shipping(type,difference):                #defining a new function named 'total_cost_of_shipping' that takes in parameters type and difference
    if type == "Regular Post Card":                        #if the parameters are met for Regular Post Card
        return(.20 + difference*.03)                        #returning the solution to equationo containg Regular Post Card cost and zone cost
    elif type == "Large Post Card":                         #if the parameters are met for Large Post Card
        return(.37 + difference*.03)                        #returning the solution to equation containing Large Post Card cost and zone cost 
    elif type == "Envelope":                                #if the parameters are met for Envelope 
        return(.37 + difference*.04)                        #returning the solution to equation containing Envelope cost and zone cost
    elif type == "Large Envelope":                          #if the parameters are met for Large Envelope
        return(.60 + difference*.05)                        #returning the solution to equation containing Large Envelope cost and zone cost
    elif type == "Package":                                 #if the parameters are met for Package
        return(2.95 + difference*.25)                       #returning the solution to equation containing Package cost and zone cot
    elif type == "Large Package":                           #if the parameters are met for Large Package
        return(3.95 + difference*.35)                      #returning the solution to equation containing Large Package cost and zone cost

main()                                                      #calling main function
