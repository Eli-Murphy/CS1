'''
Created on March 3, 2021

    Log:
        March 3: Assign date. Added menu, search and addition functions. Remove WIP, Gender Count WIP
         March 5: Search function fixed after self destruction, added while True in main
              In a constant state of pain trying to program the damn delete function, I am exhausted.
        March 8: Added city frequency counter using a dictionary
        March 11: Added different search functions including last name, city, and advisor.
        March 22: Added skeleton tightenParameter() function and added search grade function.

Bug: 

Initiative: The purpose of this project is to allow a user to modify, search, and record information about GCDS's school directory.

Bonus:

@author: EMurphy24
'''

import os
import pprint
import matplotlib.pyplot as plt
from PIL import Image 
from pygame import mixer
import time


def main():
    print("Welcome to the GCDS Directory")
    first_name = input("\nWhats the first name of the person you are looking for?: ")
    last_name = input("\nWhats the last name of the person you are looking for?: ")
    while True:
        print("If you would like to search for info on somebody by their first name, enter 'search first'.")
        print("If you would like to search for info on somebody by their last name, enter 'search last'.")
        print("If you would like to search for info on somebody by their city, enter 'search city'.")
        print("If you would like to add to the directory, enter 'modify'.")
        print("If you would like to delete an entry, enter 'delete'.")
        print("If you would like to count the frequencies of the cities enter 'city'.")
        print("If you would like to count the amount of people assigned to each advisor, enter 'advisors'.")
        print("If you would like to count genders on the list, enter 'gender'.\n")
        goto = input("Enter Here: ")
        goto == goto.lower()
        first_name = first_name.lower()                     #This isolates the first and last name for functions
        last_name = last_name.lower()
        if goto == "search first":
            print(searchF(first_name))
        elif goto == "search last":
            print(searchL(last_name))
        elif goto == "sus":
            sus()
        elif goto == "search city":
            city = input("What city are you looking for?: ")
            city = city.lower()
            print(searchCity(city))
        elif goto == "search advisor":
            advisor = input("What is the advisor's last name?: ")
            
            advisor =  '"' + advisor 
            #because the way the data is stored with a ' " ' in front of
            #the last name of the desired advisor, this adds it to allow
            #it to continue to search 
            advisor = advisor.lower()
            print(searchAdvisor(advisor))
        elif goto == "search grade":
            grade = input("What grade are you looking for? (N, PK, K, 1-12): ") 
            print(searchGrade(grade))
        elif goto == "modify":
            addition()
        elif goto == "delete":
            removal(first_name, last_name)
        elif goto == "gender":
            d = genderC()
            pprint.pprint(d)
            graph = input("Would you liked this graphed?")
            if graph == "y":
                graphing(d)
            else: continue
        elif goto == "city":
            d = cityFreq()
            pprint.pprint(d)
            #pprint is a imported print function to make a dictionary
            #look more pleasing to the user
            graph = input("Would you liked this graphed? (y/n): ")
            if graph == "y":
                plt = graphing(d)
                plt.show()
            else: continue
        elif goto == "grade":
            d = gradeFreq()
            pprint.pprint(d)
            #pprint is a imported print function to make a dictionary
            #look more pleasing to the user
            graph = input("Would you liked this graphed? (y/n): ")
            if graph == "y":
                plt = graphing(d)
                plt.show()
            else: continue
        elif goto == "advisors":
            d = advisorFreq()
            pprint.pprint(d)
            graph = input("Would you liked this graphed? (y/n): ")
            if graph == "y":
                plt = graphing(d)
                plt.show()
            else: continue
        else:
            print("Sorry! Thats not an option. Please try again.")
            main()

def searchF(first_name):
    file_in = open("datatext.txt")
    count = 0
    hold =""
    almost = ""
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
        tighten == input("Would you like to tighten the parameters by a second search? (y/n)")
        if tighten == "y":
            tightenParameters(hold)
        else:
            return hold
    file_in.close()
    
def searchL(last_name):
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[3] == last_name:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                                                                                          #if there are no found entries...
        return "No Found Person"
    elif count >= 0:
        tighten == input("Would you like to tighten the parameters by a second search? (y/n)")
        if tighten == "y":
            tightenParameters(hold)
        else:
            return hold
    file_in.close()

def searchGrade():
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    names = []
    
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[2] == grade:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                                                                                          #if there are no found entries...
        return "No Found Person"
    elif count >= 0:
        tighten == input("Would you like to tighten the parameters by a second search? (y/n)")
        if tighten == "y":
            tightenParameters(hold)
        else:
            return hold
    file_in.close()

def sus():
    sus = input("Sus? (y/n): ")
    if sus == "y":
        img = Image.open('b69.png') 
        img.show() 
        mixer.init()
        mixer.music.load('amogus.mp3')
        mixer.music.play()
        time.sleep(5)

def searchCity(city):
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[7] == city:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                                                                                          #if there are no found entries...
        return "No Found Person"
    elif count >= 0:
        tighten == input("Would you like to tighten the parameters by a second search? (y/n)")
        if tighten == "y":
            tightenParameters(hold)
        else:
            return hold
    file_in.close()

def searchAdvisor(advisor):
    file_in = open("datatext.txt")
    print(advisor)
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              #splits the line into a list at every ","
        if list_of_words[5] == advisor:                                                      #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                                                                                          #if there are no found entries...
        return "No Found Person"
    elif count >= 0:
        tighten == input("Would you like to tighten the parameters by a second search? (y/n)")
        if tighten == "y":
            tightenParameters(hold)
        else:
            return hold
    file_in.close()
    
def tightenParameters(hold):
    print("Here are your search functions to tighten parameters.\nSearch First name (SF)\nSearch Last name (SL)\nSearch Grade (SG)\nSearch City (SC)\nSearch Advisor(SA)")
    tighten = input("Input here:")
    tighten = tighten.upper()
    while True:
        if tighten == "SF":
            print("Hello")
        elif tighten == "SL":
            print("Hello")
        elif tighten == "SG":
            print("Hello")
        elif tighten == "SC":
            print("Hello")
        elif tighten == "SA":
            print("Hello")
        else:
            print("Please input the shortened version of a menu item.")
        
def addition():
    file = open("datatext.txt" , "a")                                                                     #opens the file for appending      
    first = input("first name: ")
    middle = input("middle name: ")
    last = input("last name: ")
    grade = input("grade, K for kindergarden; PK for Pre-K; and N for nursery: ")
    sex = input("M for male and F for female: ")
    teacher = input("Lastname, Firstname of the teacher (REMEMBER THE COMMA): ")
    town = input("enter town: ")
    state = input("State in two letter I.E. Connecticut = CT: ")
    zips = input("Zipcode: ")
    file.write("\n" + first + "," + middle + "," + last + "," + grade + "," + sex + "," + teacher + "," + town + "," + state + "," + zips) 
    #writes in the line to the file as a new one
    file.close()
    return "Added!"
    
def removal(first_name, last_name):
    file_in = open("datatext.txt", "r")
    file_con = file_in.read()
    file_out = open("temp.txt", "w+")
    file_out.close()
    file_out = open("temp.txt", "w")
    #lines = file.readlines()
    count = 0
    response = search(first_name, last_name)
    print(response)
    if response == "No Found Person":
         print("No Found Person")
         removal()
    for line in file_con.split('\n'):
        if response == line:
            print("113")
            file_out.write(line)
        else:
            print("116")
            count = count + 1
    if count != 0:
        print("119")
        file_in.close()
        os.replace("datatext.txt", "temp.txt")
    else:
        print("Error")
    if response == "No Found Person":
        print("No Found Person")
        removal()
    else:
        #for i in range(len(lines)):
        if any(item.lower() == response.lower() for item in lines):
            print("Hello")
        else:
            print("Fail")

def genderC():
    file_input = open("datatext.txt")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        if linelist[4] not in d:
             d[linelist[4]] = 1
        else:
             d[linelist[4]] = d[linelist[4]] + 1       
    return d


def cityFreq():
    file_input = open("datatext.txt")
    d = dict()
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
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
        
def advisorFreq():
    file_input = open("datatext.txt")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        if linelist[5] not in d:
             d[linelist[5]] = 1
        else:
             d[linelist[5]] = d[linelist[5]] + 1       
    return d

def gradeFreq():
    file_input = open("datatext.txt")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        if linelist[3] not in d:
             d[linelist[3]] = 1
        else:
             d[linelist[3]] = d[linelist[3]] + 1       
    return d

def graphing(d):
    try:
        keys = d.keys()
        values = d.values()
        
        
        x = input("What is your X-Axis?: ")
        y = input("What is your Y-Axis?: ")
    
        chart = input("Which chart would you like to use? (line, bar, or pie): ")
        if chart == "line":
            plt.plot(keys, values)
            plt.ylabel(x)
            plt.xlabel(y)
            return plt
        elif chart == "bar":
            plt.bar(keys, values)
            plt.ylabel(x)
            plt.xlabel(y)
            return plt
        elif chart == "pie":
            plt.pie(values, labels = keys, shadow=True, autopct='%1.1f%%',radius=1.3)  
            return plt
        else:
            print("Sorry! Thats not an option.")
    except:
        print("Error, missing data.")
    

# 
# def first_name(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[0])
# 
# def middle_name(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[1])
# 
# 
# def last_name(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[2])
# 
# 
# def grade(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[3])
# 
# 
# def sex(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[4])
# 
# 
# def advisor(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[5])
# 
# 
# def city(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[6])
# 
# 
# def state(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[7])
# 
# 
# def zipcode(line):
#     if line == "" or line == " ":
#         return "VOID"
#     else:
#         linelist = line.split
#         return str(linelist[8])
#                 
#                 
if __name__ == '__main__':
    main()
