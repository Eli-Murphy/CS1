'''
Created on March 3, 2021

    Log:
        March 3: Assign date. Added menu, search and addition functions. Remove WIP, Gender Count WIP
         March 5: Search function fixed after self destruction, added while True in main
              In a constant state of pain trying to program the damn delete function, I am exhausted.
        March 8: Added city frequency counter using a dictionary

Bug: Too many to count at the moment

Initiative: The purpose of this project is to allow a user to modify, search, and record information about GCDS's school directory.

Bonus:

@author: EMurphy24
'''

import os
import pprint


def main():
    print("Welcome to the GCDS Directory")
    first_name = input("\nWhats the first name of the person you are looking for?: ")
    last_name = input("\nWhats the last name of the person you are looking for?: ")
    while True:
        print("If you would like to search for info on somebody by their first name, enter 'search first'.")
        print("If you would like to search for info on somebody by their last name, enter 'search last'.")
        print("If you would like to search for info on somebody by their first and last name, enter 'search first last'.")
        print("If you would like to add to the directory, enter 'modify'.")
        print("If you would like to delete an entry, enter 'delete'.")
        print("If you would like to count the frequencies of the cities enter 'city'.")
        print("If you would like to count genders on the list, enter 'gender'.\n")
        goto = input("Enter Here: ")
        goto == goto.lower()
        first_name = first_name.lower()                     #This isolates the first and last name for  functions
        last_name = last_name.lower()
        if goto == "search first":
            print(searchF(first_name))
        elif goto == "search last":
            print(searchL(last_name))
        elif goto == "search first last":
            print(searchFL(lfirst_name, ast_name))
        elif goto == "modify":
            addition()
        elif goto == "delete":
            removal(first_name, last_name)
        elif goto == "gender":
            genderC()
        elif goto == "city":
            pprint.pprint(cityFreq())
        else:
            print("Sorry! Thats not an option. Please try again.")
            main()

def searchF(first_name):
    file_in = open("datatext.txt")
    count = 0
    hold =""
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
    
def searchL(last_name):
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[2] == last_name:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
        
    if count == 0:                                                                                          #if there are no found entries...
        return "No Found Person"
    elif count >= 0:
        return hold
    file_in.close()
    
def searchFL(first_name, last_name):
    file_in = open("datatext.txt")
    hold = ""
    count = 0
    for line in file_in:                                                                                          #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                                     #splits the line into a list at every ","
        if list_of_words[2] == last_name and list_of_words[0] == first_name:    #checks to see if words match with input
            hold = hold + "\n" + line
            count = count + 1

    if count == 0:                                                                                                 #if there are no found entries...
        return "No Found Person"
    elif count >= 0:
        return hold
    file_in.close()
    
def addition():
    file = open("datatext.txt" , "a")                                                                     #opens the file for appending      
    first = input("first name: ")
    middle = input("middle name: ")
    last = input("last name: ")
    grade = input("grade, K for kindergarden; PK for pre-kindergarden; and N for nursery: ")
    sex = input("M for male and F for female: ")
    teacher = input("Lastname, Firstname of the teacher(REMEMBER THE COMMA): ")
    town = input("enter town: ")
    state = input("State in two letter I.E. California = CA: ")
    zips = input("Zipcode: ")
    file.write("\n" + first + "," + middle + "," + last + "," + grade + "," + sex + "," + teacher + "," + town + "," + state + "," + zips) 
    #writes in the line to the file as a new one
    file.close()
    return "Added!"
    


# def removal(first_name, last_name):
#     file_in = open("datatext.txt", "r")
#     file_con = file_in.read()
#     file_out = open("temp.txt", "w+")
#     file_out.close()
#     file_out = open("temp.txt", "w")
#     #lines = file.readlines()
#     count = 0
#     response = search(first_name, last_name)
#     print(response)
#     if response == "No Found Person":
#          print("No Found Person")
#          removal()
#     for line in file_con.split('\n'):
#         if response == line:
#             print("113")
#             file_out.write(line)
#         else:
#             print("116")
#             count = count + 1
#     if count != 0:
#         print("119")
#         file_in.close()
#         os.replace("datatext.txt", "temp.txt")
#     else:
#         print("Error")
#     if response == "No Found Person":
#         print("No Found Person")
#         removal()
#     else:
#         #for i in range(len(lines)):
#         if any(item.lower() == response.lower() for item in lines):
#             print("Hello")
#         else:
#             print("Fail")
        

def genderC():
    file_input = open("datatext.txt")                                            #Opens the file
    line_count = 0
    male_count = 0
    female_count = 0
    for line in file_input:                                                       #Reads through each list
        line_count = line_count + 1
        general_split = line.split(",")                                           #creates individual lists to go through
        if general_split[4] == "M":    
            male_count = male_count + 1
        elif general_split[4] == "F":
            female_count = female_count + 1
    print("Trigger warning, this shows binary genders and does not include any other genders.")
    print("There are ", male_count, " men in the directory.")
    print("There are ", female_count, " women in the directory.")

def cityFreq():
    file_input = open("datatext.txt")
    d = dict()
    linelist =[]
    for line in file_input:
        #print(line)
        line.lower()
        linelist = line.split(",")
        #print(linelist[7])
        if linelist[7] not in d:
             d[linelist[7]] = 1
        else:
             d[linelist[7]] = d[linelist[7]] + 1       
    return d
          
    
    
    


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
