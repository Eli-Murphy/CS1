'''
Created on March 3, 2021

Log: March 3: Assign date. Added menu, search and addition functions. Remove WIP, Gender Count WIP
     March 5: Search function fixed after self destruction, added while True in main

Bug:

Initiative: The purpose of this project is to allow a user to modify, search, and record information about GCDS's school directory.

Bonus:

@author: EMurphy24
'''

import os

def main():
    print("Welcome to the GCDS Directory")
    while True:
        print("If you would like to search for info on somebody, enter 'search'.")
        print("If you would like to add to the directory, enter 'modify'.")
        print("If you would like to delete an entry, enter 'delete'.")
        print("If you would like to count genders on the list, enter 'gender'.\n")
        goto = input("Enter Here: ")
        name = input("\nWhat is your name? (First, Last): ")
        first_name = fname(name)
        last_name = lname(name)
        goto == goto.lower()
        first_name = first_name.lower()
        if goto == "search":
            print(search(name))
        #search(first_name)
        elif goto == "modify":
            addition()
        elif goto == "delete":
            removal(first_name)
        elif goto == "gender":
            genderC()


def fname(name):
    split_name = []                                     #list that holds the new word
    placeholder  = ''                                   #empty variabe to remove spaces
    for words in name:                                  #Runs the loop for the amount of words there are in the input
        if words == ' ': 
            split_name.append(placeholder)              #removes spaces and replaces it with nothing
            placeholder = ''
        else:
            placeholder += words                        #adds spaceless word into list
        return str(split_name[0])

def lname(name):
    split_name = []                                     #list that holds the new word
    placeholder  = ''                                   #empty variabe to remove spaces
    for words in name:                                  #Runs the loop for the amount of words there are in the input
        if words == ' ': 
            split_name.append(placeholder)              #removes spaces and replaces it with nothing
            placeholder = ''
        else:
            placeholder += words                        #adds spaceless word into list
        return str(split_name[1])

def search(name):
    first_name = first_name(name)
    file_in = open("datatext.txt")
   # print("Im in")
    #first_name = input("whats the first name of the person you are looking for:").lower()
    hold = ""
    count = 0
    for line in file_in: #read a line or record of info  ROW!!!
        
        line = line.lower()
        
        list_of_words = line.split(",")  #split into unique element using the delimeter ","
        #print(list_of_words)
        if list_of_words[0] == first_name:
            hold = hold + line
            count = count + 1
    if count == 0:                          #if there are no 
        return "No Found Person"
    elif count >= 0:
        return hold
    file_in.close()
      
    
def addition():
    file = open("datatext.txt" , "a")                                       #opens the file for appending      
    first = input("first name: ")
    middle = input("middle name: ")
    last = input("last name: ")
    grade = input("grade, K for kindergarden; PK for pre-kindergarden; and N for nursery: ")
    sex = input("M for male and F for female: ")
    teacher = input("Lastname, Firstname of the teacher(REMEMBER THE COMMA): ")
    town = input("enter town: ")
    state = input("State in two letter I.E. California = CA: ")
    zips = input("Zipcode: ")
    file.write("\n" + first + "," + middle + "," + last + "," + grade + "," + sex + "," + teacher + "," + town + "," + state + "," + zips) #writes in the line to the file as a new one
    file.close()
    return "Added!"
    


def removal(name):
    deleter = search(name)
    if deleter == "No Found Person":                                                               #if the request is a false
        print("no such :", name)
    else:
        file_input = open("datatext.txt")
        file_output = open("temp.txt", "w+")                                #creates a new temporary file which will contain the changes
        counter = 0
        for first_name in file_input:
            general_split = first_name.split(",")
            if general_split[0] == deleter[0] and general_split[2] == deleter[2]:
                del first_name                                                              #deletes the requested name
            else:
                file_output.write(",".join(general_split))                            #creates a long file of the strings
            counter += 1
        file_input.close()
        file_output.close()
        os.remove("datatext.txt")                                                    #Removes the original file from the algorithm
        os.rename("temp.txt", "datatext.txt")                              #Imported from OS, renames the temporary file under the name of the original file
    print("end")

def genderC():
    file_input = open("datatext.txt")                                            #Opens the file
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
    print("There are ", male_count, " men in the directory.")
    print("There are ", female_count, " women in the directory.")

    
    


def first_name(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[0])

def middle_name(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[1])


def last_name(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[2])


def grade(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[3])


def sex(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[4])


def advisor(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[5])


def city(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[6])


def state(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[7])


def zipcode(line):
    if line == "" or line == " ":
        return "VOID"
    else:
        linelist = line.split
        return str(linelist[8])
                
                
if __name__ == '__main__':
    main()
