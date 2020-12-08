'''
Created on Mar 11, 2020

@author: EMurphy24
'''
from pip._vendor.html5lib._ihatexml import letter

import os
   
##################################################################################################################################################
#Name: Eli Murphy                                                                                                                             #    
#Date of Updates:                                                                                                                      #
#Summary: My codes' function is to access certain areas of the GCDS database. It calls in the file and can either add a new person,              #
#         find a person, remove a person, or even edit a person. It has a menu function as well and it creates one giant list from               #
#         the data given and uses functions I made in the last functions project.                                                                #
#Bug(s): Some functions lack the "if NONE" statement and the first and last name when searching must be separated by a space and both            #
#        require some form of capitalization, the menu function will run infinently long, search requires the first and last                     #
#        name be capitalized, the name in search must be separated with a space, the name for search cannot contain a middle name,               #
#        the name for search must contain both the first name as well as the last name, for the additional name the comma must be                #
#        manually addded for the teacher as if it isn't then it will not be the same as the others, for the additional name if                   #
#        a section is skipped the file will mark it skipped as two commas will be next to each other, for the deletion function                  #
#        both parts of the name must be capitalized as well as exist, the deletion function requires the file exist and the name                 #
#        having a space as a separator, for deletion if two people with the same name first and last exist they will both be deleted,            #
#        for the update function the name must be there as in exist to work, the update function will allow any value to be changed to anything, #
#        if the user prompts a number higher than 8 being a number that doesn't have a position and adds a value for it then it will             #
#        add that value but cause the next string to be joined with that string                                                                  #
#Log: The deletion function seemingly lacked the ability to delete the full line, the update function would make a copy and implement            #
#     that copy as an additional name, the update function wouldn't write in the new name and would break, the update function would             #
#     only write in the new name and remove everything else, the update function would remove the entire data, the update function               #
#     would seemingly break at line 151 where "pop" was originally "remove"                                                                      #
##################################################################################################################################################
def first_name(name):
    #Imported from another code whihc takes the parameters
    #of name and counts each char until it reaches a space
    #and when it reaches the space it will return the first
    #word under retain by placing each letter, or char,
    #in retain up until the space
    retain = ''
    for letter in name:
        if letter == ' ':
            break
        else:
            retain = retain + letter
    return retain
       

def reverse(name):
    #Imported from another code which takes the parameters
    #of the name and simple starts from the last char and
    #moves backwards placing each char in output
    output = ''
    counter = len(name) - 1
    while(counter >= 0):
        output = output + name[counter]
        counter = counter - 1
    return output

def last_name(name):
    #Imported from another code which takes the parameters
    #writes the name from the back until a space and then
    #reverses what it wrote
    count = len(name) -1
    output = ''
    while count >= 0:
        if (name[count] == ' '):
            break
        else:
            output = output + name[count]
            count = count - 1
    return reverse(output)



def gender_count():
    file_input = open("gcds_data.csv")                                           #Opens the file
    line_count = 0
    male_count = 0
    female_count = 0
    for job in file_input:                                                       #Reads through each list
        line_count = line_count + 1
        general_split = job.split(",")                                           #creates individual lists to go through
        if general_split[4] == "M":    
            male_count = male_count + 1
        elif general_split[4] == "F":
            female_count = female_count + 1
    print(male_count)
    print(female_count)


def search(name):
    """Gets an identifier and returns a list.
   
    The function will assign a value for the variables, 'first' and 'last' where they are the first name of the requested name
    and the last name of the requested person. The function then opens up the csv file title gcds_data.csv which contains the
    information regarding the students at the Greenwich Country Day School. It proceeds to go through string by string of the students
    as it returns a list of all the values in the string, using str ',' as the separator. It will ask if the the values in position 0
    which is the first name of the list is the same as the variable first storing the desired first name and compares the value in
    position 2 which is the last name with the variable last storing the desired last name. When the two values correspond, the
    function will return the string of the requested subject.
   
        Typical usage example:
            first = first_name()
            last = last_name()
            general_split = str.split('')
           
    Args:
        Name: String of the requested subject
       
    Returns:
        General_Split: String containing the requested user's information
       
    Raises:
        1 - Name, both first and last, need to be capitolized
        2 - Names must be separated by a space
        3 - Name cannot contain a middle name in it
        4 - Name must contain both first, and last
       
   
    """
    first = first_name(name)
    last = last_name(name)
    file_input = open("gcds_data.csv")
    for name in file_input:
        #Runs through each string in the file line by line
        general_split = name.split(",")
        if general_split[0] == first and general_split[2] == last:                 #if the individual list present is identicle to the request of the user
            #Compare the position of general_split
            #which is the list of the persons info-
            #rmation with the users requested inp-
            #ut to see if the first and last name
            #in the list correspond with the users
            #request
            return(general_split)
           




def additional_name():    
    """Takes a variable and returns a string.
   
    The function opens the csv data sheet titled gcds_data.csv and opens it up for appending. It
    proceeds to request the user for designated values for the information required to add a new
    string to the data set. Upon prompt, the user enters each one of their desired values as the
    function proceeds then to write in the values as a string which is then added to the data
    set. Upon completion the function closes out the data set allowing the additions to allocate
    to the permanent memory. In summary, this function takes a group of variables and creates a new
    string to be added to the data set so users may add in new clients.
   
    Args:
        NONE
       
    Returns:
        String containing the vars of the users new name
       
    Raises:
        1 - If the comma in the name is not implimented, then it will not correlate with the others in the file
        2 - If the section is skipped, it will go to the next one with two commas
   
   
    """                                                          
    file_output = open("gcds_data.csv" , "a")                                       #opens the file for appending      
    first = input("first name: ")
    middle = input("middle name: ")
    last = input("last name: ")
    grade = input("grade, K for kindergarden; PK for pre-kindergarden; and N for nursery: ")
    sex = input("M for male and F for female: ")
    teacher = input("Lastname, Firstname of the teacher(REMEMBER THE COMMA): ")
    town = input("enter town: ")
    state = input("State in two letter I.E. California = CA: ")
    zips = input("Zipcode: ")
    file_output.write(first + "," + middle + "," + last + "," + grade + "," + sex + "," + teacher + "," + town + "," + state + "," + zips ) #writes in the line to the file as a new one
    file_output.close()                                                              #closes the file to allow the edits to change
   


def deletion (name):
    """Takes an identifier and removes a string from a csv.
   
    Prompted by the user, the function will set the list of the identified target in the variable
    'deleter'. However, if the list doesn't exist, then the function will return a statement informing
    the user that their target does not exist in the list. If the user does exist, the function will open
    the csv data set gcds_data.csv and creates a temporary file dubbed gcds_data_temp.csv through granting
    the function permission by using w+. The function proceeds to create a counter for each time it goes
    through a string and proceeds to read the gcds_data csv string by string as it returns a list of all
    the values in the string, using str ',' as the separator. If the positions of the deleter list and the
    current list being read through are equal, the function will delete that requested name, more specifically
    deleter. If not, it will add the string to a long file of all the strings being stored in the created
    temporary, gcds_data_temp.csv, file as it will undo the splitting of the strings reverting the list back
    to a string. When the function has completed running through every string, it will close out both data
    sets and it will remove the original file, gcds_data, from the algorithm. The function finishes off by
    renaming the temporary file to the name of the original file through using the imported function from
    os 'remove' and 'rename.' The file at hand will then have all but that one name included in the set.
   
    Args:
        Name: Name of the requested subject
       
    Returns:
        Gcds_data.csv: file containing string of all users excluding the requested subject
       
    Raises:
        1 - Must be capitolized
        2 - Must exist
        3 - Name must be separated by a space
        4 - File must exist
        5 - If two people have the same first and last name and that name is chosen, it will remove both
   
    """
    deleter = search(name)
    if deleter is None:                                                               #if the request is a false
        #This will check to ensure that
        #the requested name exists and
        #if it doesn't, then it will
        #inform the user that no such
        #name exists
        print("no such :", name)
    else:
        file_input = open("gcds_data.csv")
        file_output = open("gcds_data_temp.csv", "w+")                                #creates a new temporary file which will contain the changes
        counter = 0
        for name in file_input:
            #For each string in the file, it will
            #create an individual list from each
            #string using the comma as a separator
            #as it runs through each list in the file
            general_split = name.split(",")
            if general_split[0] == deleter[0] and general_split[2] == deleter[2]:
                #If the 0th position, first char, which is the first name
                #is the same as the requested person's file at the same
                #position and if the 2nd position of the current file that
                #is being ran through which is the last name is equal to the
                #same last name as the requested person's file, then it will
                #delete that file as the two are one of the same
                del name                                                              #deletes the requested name
            else:
                #If it is not the name, it will put the
                #file at hand back into a long file of the strings
                #so that when it comes time to write back
                #the file, all but the requested one will
                #be present in it
                file_output.write(",".join(general_split))                            #creates a long file of the strings
            counter += 1
        file_input.close()
        file_output.close()
        os.remove("gcds_data.csv")                                                    #Removes the original file from the algorithm
        os.rename("gcds_data_temp.csv", "gcds_data.csv")                              #Imported from OS, renames the temporary file under the name of the original file


     
def update (name):
    """Takes an identifier and returns an augmented string to a file.
   
    The function will open the file, gcds_data.csv, with permission for the function to
    read and write into the file through using r+. The function proceeds to create one
    giant list of all the students from the file as it proceeds to close set file. After
    re-opening the file and granting it permission to write over the exiting file through
    its usage of w+. The function proceeds to print out a number of instruction informing
    the user of their options as it goes on to store their response as an int under the var
    of update_option hence prompting the user to then type their desired char of which the
    value is stored under the variable new_value. The function then reads through each string
    in the file one by one as it creates an individual list from each student's values in the
    string using str ',' as a separator. When the function, much like that of the search function,
    identifies the corresponding list by their corresponding positions, it will, based off of the
    users choice, set that position in the found list equal to the value stored as new_value. The
    function then proceeds to turn the list into a string and, by using the pop function, remove and replace the
    original record being stored as record_found_location. The function will then impliment the new
    string into the file containing the remaining strings. If the name is not found however, the var
    record_found_location will increase by one. The function will then, before closing out the file,
    use the command 'writelines' to move all of the records from the temporary storage, RAM, into the
    permanent stored memory which is either the HDD or SSD depending on the users setup. Finally, the
    function will close the file out as a whole thus ending the updates.
   
    Args:
        name: Name of the requested subject, moreover, their file
       
    Returns:
        all_students: returns a string of all the students
        student_data: returns a file post-modification
       
    Raises:
        1 - if the name is not there, it will still operate but not transcribe
        2 - Name must exist and be first space last both capitolized
        3 - It will allow a value to be replaced that doesn't make sense
        4 - It will not work if the file has been deleted
        5 - If it is in the 9th... place, it will add another value and cause the next string on the list to be attached to it
   
    """
    found = False
    record_found_location = 0
    file_input = open("gcds_data.csv", "r+")                                           #This line will open the file with permission to read and write
    all_students = file_input.readlines()                                              #Creates one giant list of all of the students from the file
    file_input.close()
    file_output = open("gcds_data.csv", "w+")                                          #Re-opens the file allowing us to over write the existing file
    print("If you are updating the first name, press '0' ")
    print("If you are updating the middle name, press '1' ")
    print("If you are updating the last name, press '2' ")
    print("If you are updating the grade, press '3' ")
    print("If you are updating the sex, press '4' ")
    print("If you are updating the teacher, press '5' ")
    print("If you are updating the town, press '6' ")
    print("If you are updating the state, press '7' ")
    print("If you are updating the zip code, press '8' ")
    update_option = int(input("Type here: "))                                           #the user will select which option they want
    new_value = input("Please enter new value: ")
    for dude in all_students:
        #For dude, the student string, in the file
        #containing all of the students; it will create
        #an individual list for dude, each student, as it
        #will return a list from string dude
        student_data = dude.split(",")                                                  #creates an individual list from each student as split will return a list  
        if first_name(name) == student_data[0] and last_name(name) == student_data[2]:
            #Checks to see if the first name of the requested user is that of the
            #current student's list going through and the last name of the reques-
            #ted user is that of the current student's lists' last name is the same
            #by implimenting the first_name function to isolate the first bit of the
            #manually imputted part and the function last_name to isolate the last bit
            #being the name of the manually imputted part. Then, based off the users
            #int the placed in which coorelates with the pos of the desired change,
            #the value of that position becomes the users desired value of that pos
            #by setting the pos equal to the users choice. Once the correct record
            #is found, the bool will become True indicating the coorespondance.
            #Then, changed_record-as_string will revert the list back into its
            #string as it will be joined by str comma. After the reverting is
            #completed, it will remove the original file and will insert the records
            #into the new file which will be the one containing the changes.
            student_data[update_option] = new_value                                     #based off of the users decision/choice, the position they selected in the list will be altered
            found = True                                                                #Once the correct record is found, it will set the boolean to true for update/delete/insert
            changed_record_as_string = ",".join(student_data)                           #this will turn the list into a string
            all_students.pop(record_found_location)                                     #this line will remove the prior, unedited, raw, record
            all_students.insert(record_found_location, changed_record_as_string)        #this will insert the new record which contains the changes  
            break
        else:
            record_found_location += 1      
    file_output.writelines(all_students)                                                #moves the records from the RAM to either the HDD or SSD
    file_output.close()
       

def main():
    """Takes a char and returns a functional output.
   
    This function is really quite simple as it will give the user four prompts
    of which the user will type in one of those given prompts which will then
    be stored as menu_option variable. The function will then compare the given
    variable to a number of potential responses to see if they are the same. If
    so, it will call the function listed below it.
   
    Args:
        None
       
    Returns:
        Additional_name: file containing a new string
        Search: Prints a file of code
        Deletion: file excluding a singular string upon request
        Update: file that has been modified with new changes to a string
       
    Raises:
        1 - it will run infinently
        2 - it will send you back to the print statements if the choice is not valid
   
    """
    while 1 == 1:
        print("Welcome to the GCDS database; here you can access the GCDS data")
        print("If you want to search someone up, type in 'search' ")
        print("If you want to add information to the database, type in 'add' ")
        print("If you want to remove someone from the database, type in 'delete' ")
        print("If you want to update information in the database, type in 'update' ")
        menu_option = input("Type here: ")
        if menu_option == "add":
            #If the users choice for menu_option
            #is "add," then it will call upon
            #the additional_name function to
            #run
            additional_name()
        elif menu_option == "search":
            #If the users choice for menu_option
            #is "search," then it will request you
            #a name to add in which that input will
            #run through the search function as the arg
            #and will print out the file with similar first
            #and last name values with the input
            name = input("Please enter the name of whom you wish to learn about: ")
            search(name)
            print(search(name))
        elif(menu_option == "delete"):
            #If the users choice for menu_option
            #is "delete," then it will prompt the
            #user for an input of the name parameters
            #which will serve as the arg for the function
            #deletion which it will then call upon
            name = input("Please enter the name of whom you wish to delete: ")
            deletion(name)
        elif(menu_option == "update"):
            #If the users choice for menu_option
            #is "update," then it will prompt the
            #user for an input of their desired name
            #as an input of the name parameters which
            #will serve as the arg for the function
            #update as it calls upon the function
            #for name to be ran through
            name = input("Please enter the name of whom you wish to update: ")
            update(name)


if __name__ == '__main__':
    main()
