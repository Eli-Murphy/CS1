'''
Created on March 3, 2021

    Log:
        March 3: Assign date. Added menu, search and addition functions. Remove WIP, Gender Count WIP
         March 5: Search function fixed after self destruction, added while True in main
              In a constant state of pain trying to program the damn delete function, I am exhausted.
        March 8: Added city frequency counter using a dictionary
        March 11: Added different search functions including last name, city, and advisor.
        March 22: Added skeleton tightenParameter() function and added search grade function.
        March 29: Removed the remove() function because it didnt work at all
                         Cleaning up and formating
        March 30: Hold the phone Houston we have a working remove() function praise jesus
                        Still working on that tighten parameters, need to figure out a way to compare list items...
        April 1: Finished tightenParameters() function
        April 6: Removed unnecesarry inputs
        April 7: Added HTML website to hold responses
        April 8-9: Polished up HTML code
        April 20: Happy 4/20, Added Local log recording, added true or false for auto opening
                       Added password protection for delete(), addition(), update()
        April 21: Added Username and Password adder
        April 22: Cleaned up code and added documentation

Bug: 
    March 30: There is a problem with the remove function where due to python holding the datatext.txt in RAM, it cannot fully run without manually clearing processes in procexp.exe
    April 1: Had to hardcode a fix, in tightenParameters() fuction, for some reason there is a blank string in a hold list which results in a second unwanted match.
                Update: Hardcode approved by Campbell
    April 9: Sometimes some of the HTML is overwritten, despite everything being written in append mode
                 Update: FIXED

Initiative: The purpose of this project is to allow a user to modify, search, and record information about GCDS's school directory.

Bonus: HTML Output

@author: EMurphy24
'''

#Required Libraries 
import os
import matplotlib.pyplot as plt
import re
from datetime import datetime
import webbrowser
from pathlib import Path


#Global Variables
scount = 1
fcount = 1
dcount = 1
acount = 1
tcount = 1
ucount = 1
results = ""
access = False


autohtml = False


def main():
    print("Welcome to the GCDS Directory ||| Created by Eli Murphy ||| All actions are logged on local machine ")
    first_name = input("\nWhats the first name of the person you are looking for?: ")
    last_name = input("\nWhats the last name of the person you are looking for?: ")
    webdude = open(r"C:\inetpub\wwwroot\temp.txt", "w")
    now = datetime.now()
    global results
    today = now.strftime("%B %d, %Y  ||| %H:%M:%S")
    #Formats the date
    today = today.upper()
    header = "<header><h4><b>ELI MURPHY HTML DATABASE OUTPUT   ///    ALL DATA IS ERASED AFTER CODE IS RUN AGAIN   ///   DATE AND TIME OF RECORD: " + str(today) + "</b></h4></header><br>"
    results = header + results
    if autohtml:
        webbrowser.open_new_tab('http://10.51.20.70/database.html')
    webdude.close()
    
    #adds header and date to the HTML output
    while True:
        print("  Please enter one of the cooresponding numbers. (1-15) ")
        print("  (1)  Search for info on somebody by their first name.")
        print("  (2)  Search for info on somebody by their last name.")
        print("  (3)  Search for info on somebody by their advisor.")
        print("  (4)  Search for info on somebody by their city.")
        print("  (5)  Search for info on somebody by their grade.")
        print("  (6)  Add to the directory.")
        print("  (7)  Update a already created entry.")
        print("  (8)  Delete an entry.")
        print("  (9)  Count the frequencies of the cities.")
        print("  (10)  Count the frequencies of the states.")
        print("  (11)  Count the amount of people assigned to each advisor.")
        print("  (12)  Count genders on the directory.")
        print("  (13)  Count grades on the directory")
        print("  (14)  Create an admin account.")
        print("  (15)  Rename searched person.\n")
        goto = input("Enter Here: ")
        goto = goto.lower()
        first_name = first_name.lower()                     #This isolates the first and last name for functions
        last_name = last_name.lower()
        
        
        if goto == "1":
            #All other search elifs are built almost exactly like this
            #take this documentation for all of these search elifs
            hold = searchF(first_name)
            print(hold)
            incoming = "search"
            webRecord(incoming, hold)
            #This records the output to the local logs and HTML logs
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                #This combines two search functions
                print(hold)
                incoming = "tight"
                webRecord(incoming, hold)
                #This records the output to the local logs and HTML logs
            else:
                print("Please input y or n.")
                
                
        elif goto == "2":
            hold = searchL(last_name)
            print(hold)
            incoming = "search"
            webRecord(incoming, hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
                incoming = "tight"
                webRecord(incoming, hold)
            else:
                print("Please input y or n.")


        elif goto == "4":
            city = input("What city are you looking for?: ")
            city = city.lower()
            hold = searchCity(city)
            print(hold)
            incoming = "search"
            webRecord(incoming, hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
                incoming = "tight"
                webRecord(incoming, hold)
            else:
                print("Please input y or n.")


        elif goto == "3":
            advisor = input("What is the advisor's last name?: ")
            
            advisor =  '"' + advisor 
            #because the way the data is stored with a ' " ' in front of
            #the last name of the desired advisor, this adds it to allow
            #it to continue to search 
            advisor = advisor.lower()
            hold = searchAdvisor(advisor)
            print(hold)
            incoming = "search"
            webRecord(incoming, hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
                incoming = "tight"
                webRecord(incoming, hold)
            else:
                print("Please input y or n.")


        elif goto == "5":
            grade = input("What grade are you looking for? (N, PK, K, 1-12): ") 
            hold = searchGrade(grade)
            print(hold)
            incoming = "search"
            webRecord(incoming, hold)
            tighten = input("Would you like to tighten your parameters? (y/n): ")
            if tighten == "y":
                hold = tightenParameters(hold, first_name, last_name)
                print(hold)
                incoming = "tight"
                webRecord(incoming, hold)
            else:
                print("Please input y or n.")


        elif goto == "6":
            if access == False:
                print("THIS AREA IS PASSWORD PROTECTED. PLEASE INPUT USERNAME AND PASSWORD")
                username = input("Username: ")
                password = input("Password: ")
                grant = accounts(username, password)
                #this allows makes sure no accounts are added accidentally
                if grant:
                    hold = addition()
                    #adds person to database
                    print("Added!")
                    incoming = "add"
                    webRecord(incoming, hold)
                    #This records the output to the local logs and HTML logs
                else:
                    print("Sorry! Incorrect password!")
            else:
                 hold = addition()
                 #adds person to database
                 print("Added!")
                 incoming = "add"
                 webRecord(incoming, hold)
                #This records the output to the local logs and HTML logs
            
            
        elif goto == "8":
            if access == False:
                print("THIS AREA IS PASSWORD PROTECTED. PLEASE INPUT USERNAME AND PASSWORD")
                username = input("Username: ")
                password = input("Password: ")
                grant = accounts(username, password)
                #this allows makes sure no accounts are added accidentally
                if grant:
                    hold = delete(first_name, last_name)
                    #deletes person from database
                    incoming = "del"
                    webRecord(incoming, hold)
                    #This records the output to the local logs and HTML logs
                else:
                    print("Sorry! Incorrect password!")
            else:
                hold = delete(first_name, last_name)
                #deletes person from database
                incoming = "del"
                webRecord(incoming, hold)
                #This records the output to the local logs and HTML logs

        elif goto == "7":
            if access == False:
                print("THIS AREA IS PASSWORD PROTECTED. PLEASE INPUT USERNAME AND PASSWORD")
                username = input("Username: ")
                password = input("Password: ")
                grant = accounts(username, password)
                #this allows makes sure no accounts are updated accidentally
                if grant:
                    hold = update(first_name, last_name)
                    #updates person in database
                    incoming = "update"
                    webRecord(incoming, hold)
                    #This records the output to the local logs and HTML logs
                else:
                    print("Sorry! Incorrect password!")
            else:
                hold = update(first_name, last_name)
                #updates person in database
                incoming = "update"
                webRecord(incoming, hold)
                #This records the output to the local logs and HTML logs
                
                

        elif goto == "12":
            d = genderC()
            #this gets the frequency of each gender
            print(d)
            #This prints the frequency
            incoming = "freq"
            hold = d
            webRecord(incoming, hold)
            #This records the output to the local logs and HTML logs
            graph = input("Would you liked this graphed?")
            while True:
                if graph == "y":
                    plt = graphing(d)
                    #This sends the directory to a function to be graphed
                    try:
                        plt.show()
                        break
                    except:
                        print("Graphing Error")
                elif graph == "n":
                    print("Please input either y or n. ")
                else: break
            
            
        elif goto == "9":
            d = cityFreq()
            #this gets the frequency of each city
            print(d)
            #This prints the frequency
            incoming = "freq"
            hold = d
            webRecord(incoming, hold)
            #This records the output to the local logs and HTML logs
            graph = input("Would you liked this graphed? (y/n): ")
            while True:
                if graph == "y":
                    plt = graphing(d)
                    #This sends the directory to a function to be graphed
                    try:
                        plt.show()
                        break
                    except:
                        print("Graphing Error")
                elif graph == "n":
                    print("Please input either y or n. ")
                else: break
            
            
        elif goto == "13":
            d = gradeFreq()
            #this gets the frequency of each grade
            print(d)
            #This prints the frequency
            incoming = "freq"
            hold = d
            webRecord(incoming, hold)
            #This records the output to the local logs and HTML logs
            graph = input("Would you liked this graphed? (y/n): ")
            while True:
                if graph == "y":
                    plt = graphing(d)
                    #This sends the directory to a function to be graphed
                    try:
                        plt.show()
                        break
                    except:
                        print("Graphing Error")
                elif graph == "n":
                    print("Please input either y or n. ")
                else: break
            
            
        elif goto == "11":
            d = advisorFreq()
            #this gets the frequency of each advisor
            print(d)
            #This prints the frequency
            incoming = "freq"
            hold = d
            webRecord(incoming, hold)
            #This records the output to the local logs and HTML logs
            graph = input("Would you liked this graphed? (y/n): ")
            while True:
                if graph == "y":
                    plt = graphing(d)
                    #This sends the directory to a function to be graphed
                    try:
                        plt.show()
                        break
                    except:
                        print("Graphing Error")
                elif graph == "n":
                    print("Please input either y or n. ")
                else: break
            
            
        elif goto == "10":
            d = stateFreq()
            #this gets the frequency of each state
            print(d)
            #This prints the frequency
            incoming = "freq"
            hold = d
            webRecord(incoming, hold)
            #This records the output to the local logs and HTML logs
            graph = input("Would you liked this graphed? (y/n): ")
            while True:
                if graph == "y":
                    plt = graphing(d)
                    #This sends the directory to a function to be graphed
                    try:
                        plt.show()
                    except:
                        print("Graphing Error")
                elif graph == "n":
                    print("Please input either y or n. ")
                else: break                
        
        elif goto == "15":
            yn = input("Doing this will wipe the HTML log. Continue? (y/n): ")
            while True:
                if yn == "y":
                    main()
                elif yn == "n": break
                else: 
                    print("Please input either y or n.")
                    
        
        elif goto == "14":
            createAccount()
            
            
        else:
            print("Sorry! Thats not an option. Please try again.")

def searchF(first_name):
    file_in = open("datatext.txt")
    count = 0
    hold =""
    almost = ""
    for line in file_in: 
    #read a line or record of info  ROW!!!
        line = line.lower()
        list_of_words = line.split(",")  
        #split into unique element using the delimeter ","
        if list_of_words[0] == first_name:
            hold = hold + line
            count = count + 1
    if count == 0:
    #if there are no results
        return "No Found Person"
    else:
        return hold
        
    file_in.close()
    
def searchL(last_name):
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    names = []
    for line in file_in:
    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")
        #splits the line into a list at every ","
        if list_of_words[2] == last_name:                                                      
        #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
    if count == 0:                         
    #if there are no results
        return "No Found Person"
    else:
        return hold
        
    file_in.close()

def searchGrade(grade):
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    names = []
    
    for line in file_in:
    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",") 
        #splits the line into a list at every ","
        if list_of_words[2] == grade:
        #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
            
    if count == 0:
    #if there are no results
        return "No Found Person"
    else:
        return hold
        
    file_in.close()

def searchCity(city):
    file_in = open("datatext.txt")
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    
    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                              
        #splits the line into a list at every ","
        if list_of_words[7] == city:                                                      
        #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
            
    if count == 0:                          
    #if there are no results
        return "No Found Person"
    else:
        return hold
        
    file_in.close()
    
def searchAdvisor(advisor):
    file_in = open("datatext.txt")
    print(advisor)
    count = 0
    hold = ""
    names = []
    for line in file_in:                                                                                    
    #a loop for every line in the text file
        
        line = line.lower()
        
        list_of_words = line.split(",")                                                            
        #splits the line into a list at every ","
        if list_of_words[5] == advisor:                                                     
        #checks to see if words match with input
            hold = hold + line
            count = count + 1
    
        
           
    if count == 0:                         
    #if there are no results
        return "No Found Person"
    else:
        return hold
        
    file_in.close()

def tightenParameters(hold, first_name, last_name):
    print("Here are your search functions to tighten parameters.\nSearch First name (SF)\nSearch Last name (SL)\nSearch Grade (SG)\nSearch City (SC)\nSearch Advisor(SA)")
    tighten = input("Input here:")
    tighten = tighten.upper()
    hold1 = hold
    final = ""
    if tighten == "SF":
        print("\n")
        hold2 = searchF(first_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        try:
            hold1list.remove("")
            hold2list.remove("")
            #this is a temporary hardcode problem 
            #to remove the empty piece of data made 
            #in the lists above
        except:
            print("No results")
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
            
    elif tighten == "SL":
        print("\n")
        hold2 = searchL(last_name)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        try:
            hold1list.remove("")
            hold2list.remove("")
            #this is a temporary hardcode problem 
            #to remove the empty piece of data made 
            #in the lists above
        except:
            print("No results")
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    elif tighten == "SG":
        grade = input("What grade are you looking for?: ")
        print("\n")
        hold2 = searchGrade(grade)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        try:
            hold1list.remove("")
            hold2list.remove("")
            #this is a temporary hardcode problem 
            #to remove the empty piece of data made 
            #in the lists above
        except:
            print("No results")
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    elif tighten == "SC":
        city = input("What city are you looking for?: ")
        print("\n")
        hold2 = searchCity(city)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        try:
            hold1list.remove("")
            hold2list.remove("")
            #this is a temporary hardcode problem 
            #to remove the empty piece of data made 
            #in the lists above
        except:
            print("No results")
        
        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
    elif tighten == "SA":
        advisor = input("What advisor are you looking for?: ")
        print("\n")
        hold2 = searchAdvisor(advisor)
        hold1list = hold1.split("\n")
        hold2list = hold2.split("\n")
        try:
            hold1list.remove("")
            hold2list.remove("")
            #this is a temporary hardcode problem 
            #to remove the empty piece of data made 
            #in the lists above
        except:
            print("No results")

        for i in hold1list:
            for j in hold2list:
                if i == j:
                #if there is a match in the list,
                    final = final + i + "\n"
                    #add it to the return string
        if final == "":
            return "Sorry, no found matches!\n"
        else:
            return final
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
    hold = "\n" + first + "," + middle + "," + last + "," + grade + "," + sex + "," + '"' + teacher + '"' +"," + town + "," + state + "," + zips
    file.write(hold)
    #writes in the line to the file as a new one
    file.close()
    return hold

def delete(first_name, last_name):
    input_file = open("datatext.txt", "r")
    output_file = open("temp.txt", "w")
    hold = ""
    #This fixes the problem of miscapitalization.
    count = 0
    for line in input_file:
        line = line.lower()
        data = line.split(",")
        #this splits the line at the comma, making a list
        if data[0] == first_name and data[2] == last_name:
        #if the first item in the line matches with the first name and the 3rd item in the line matches with the last name,
            count = count + 1
            hold = hold + line + "<br>"
            continue
        else:
            output_file.write(line)
            #writes the lines not containing the deleted party
    if count > 0:
        input_file.close()
        output_file.close()
        os.remove("datatext.txt")
        os.rename("temp.txt", "datatext.txt")
        output_file.close()
        print("Done!")
        return hold
    else:
        print("Sorry, no results found.")

def update(first_name, last_name):
    dhold = delete(first_name, last_name)
    print("\nNow, rewrite the user's info.\n")
    ahold = addition()
    returning = []
    returning.append(dhold)
    returning.append(ahold)
    return returning

def genderC():
    file_input = open("datatext.txt")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        #This converts the line to a list and makes a new item 
        #at every ','
        if linelist[4] not in d:
        #if the fifth (items in lists start at a 0) item in the menu
         #isnt in the directory
             d[linelist[4]] = 0
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
        line.lower()
        linelist = line.split(",")
        #This converts the line to a list and makes a new item 
        #at every ','
        if linelist[7] not in d:
        #if the eight  (items in lists start at a 0) item in the menu
         #isnt in the directory    
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
        #if the sixth (items in lists start at a 0) item in the menu
        #isnt in the directory
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
         #if the fourth (items in lists start at a 0) item in the menu
         #isnt in the directory   
             d[linelist[3]] = 1
        else:
             d[linelist[3]] = d[linelist[3]] + 1       
    d = dict(sorted(d.items(), key=lambda d: d[1], reverse=True))
    print(str(d))
    return d

def stateFreq():
    file_input = open("datatext.txt")
    d = dict() 
    #this creates a dictonary under variable name 'd'
    #this makes organizing the freqency significantly easier.
    linelist =[]
    for line in file_input:
        line.lower()
        linelist = line.split(',')
        if linelist[8] not in d:
         #if the fourth (items in lists start at a 0) item in the menu
         #isnt in the directory   
             d[linelist[8]] = 1
        else:
             d[linelist[8]] = d[linelist[8]] + 1        
    d = dict(sorted(d.items(), key=lambda d: d[1], reverse=True))
    return d

def graphing(d):
    try:
        keys = d.keys()     
        values = d.values()
        #this separates the matching keys and values to its own 
        #variables, making it easier to work with
        
        
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
            #To be honest, im not sure what all these mean, but I do know that this 
            #customizes the pie chart.
            return plt
        else:
            print("Sorry! Thats not an option.")
    except:
        print("Error, missing data.")

def webRecord(incoming, hold):
    global results
    #global localresults
    #This makes sure the results dont get overwritten by the new texta
    if incoming == "search":
        
        hold_re = repr(hold)
        #turns the string into a RE, making the "\n" in the string and able
        #to be removed and replaced by the HTML equivelant
        hold_re = hold.replace("\n", "<br>")
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        global scount
        #Makes sure the number of results dosent change when the function is rerun
        results = results + "<b>Search Results #" + str(scount) + "</b><br><br>" + hold_re + "<br>"
        #this is for HTML logs
        webdude.write(results)
        webdude.close()
        scount = scount + 1
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot\temp.txt", "C:\inetpub\wwwroot\database.html")
        #deletes the database file in there, and renames the text file to HTML
        
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Search Results\n\n\n" + hold + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\DayLog " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)

    
    elif incoming == "freq":
        
        global fcount
        #Makes sure the number of results dosent change when the function is rerun
        hold = str(hold)
        
        hold = hold.replace(",", "<br>")
        hold = hold.replace("{", "")
        hold = hold.replace("}","")
        #makes the dictionary better to read
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        results = results + "<b>Frequency Results #" + str(fcount) + "</b><br><br>" + hold + "<br><br>"
        webdude.write(results)
        fcount = fcount + 1
        webdude.close()
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot/temp.txt", "C:\inetpub\wwwroot\database.html")
        #deletes the database file in there, and renames the text file to HTML
        
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Frequency Results\n\n\n" + hold + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\DayLog " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)
        
    elif incoming == "del":
        global dcount
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        results = results + "<b>Deleted Entry/ies #" + str(dcount) + "</b><br><br>" + str(hold) + "<br><br>"
        webdude.write(results)
        webdude.close()
        dcount = dcount + 1
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot\temp.txt", "C:\inetpub\wwwroot\database.html")
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Delete Entry/ies\n\n\n" + str(hold) + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\DayLog " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)
        
    elif incoming == "add":
        global acount
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        results = results + "<b>Added Entry #" + str(acount) + "</b><br><br>" + hold + "<br><br>"
        webdude.write(results)
        webdude.close()
        acount = acount + 1
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot\temp.txt", "C:\inetpub\wwwroot\database.html")
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Added Entry\n\n\n" + hold + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\DayLog " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)
        
    elif incoming == "tight":
        hold_re = repr(hold)
        #turns the string into a RE, making the "\n" in the string and able
        #to be removed and replaced by the HTML equivelant
        hold_re = hold.replace("\n", "<br>")
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        global tcount
        #Makes sure the number of results dosent change when the function is rerun
        results = results + "<b>Search Results #" + str(tcount) + "</b><br><br>" + hold_re + "<br>"
        webdude.write(results)
        webdude.close()
        tcount = tcount + 1
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot\temp.txt", "C:\inetpub\wwwroot\database.html")
        #deletes the database file in there, and renames the text file to HTML
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Tightened Results\n\n\n" + hold + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\DayLog " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)
    elif incoming == "update":
        dhold = hold[0]
        ahold = hold[1]
        global ucount
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        results = results + "<b>Updated Entry #" + str(ucount) + "</b><<br>" + str(dhold) + "<br><br> " + "Was replaced with: " + "<br><br>" + str(ahold) + "<br><br>"
        webdude.write(results)
        webdude.close()
        ucount = ucount + 1
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot\temp.txt", "C:\inetpub\wwwroot\database.html")
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Updated Entry\n\n\n" + str(dhold) + "\n\nWas replaced with: \n\n" + str(ahold) + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\log " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)
    elif incoming == "newuser":
        webdude = open(r"C:\inetpub\wwwroot\temp.txt", "a")
        results = results + "<b>Added Account</b><br>" + hold + "<br><br>"
        webdude.write(results)
        webdude.close()
        acount = acount + 1
        os.remove(r"C:\inetpub\wwwroot\database.html")
        os.rename(r"C:\inetpub\wwwroot\temp.txt", "C:\inetpub\wwwroot\database.html")
        
        #Below logs all acts locally in text files
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        localresults = "["+ time +"] Added Account\n\n" + hold + "\n\n"
        today = now.strftime("%b, %d, %y")
        logdate = r"C:\\database logs\\DayLog " + str(today) + r".txt"
        #path to files
        my_file = Path(logdate)
         #this turns the path to be read by .is_file()
        if my_file.is_file():
            log = open(logdate, "a")
        else:
            log = open(logdate, "w+")
            #creates a file
            log.close
            log = open(logdate, "a")
        log.write(localresults)

def accounts(username, password):
    #true = 0
    status = False
    accounts = open(r"C:\database logs\accounts.txt")
    for line in accounts:
        line = line.strip()
        list_of_words = line.split(",")                                                              
        #splits the line into a list at every ","
        print(list_of_words)
        if list_of_words[0] == username and list_of_words[1] == password:
            global access
            #this allows the user to only have to log in once
            access = True
            return True
            
def createAccount():
    newuser = input("\nNew Username: ")
    newpass = input("\nNew Password: ")
    conpassword = input("\nConfirm New Password: ")
    username = input("\n\nInput Current Admin Username: ")
    password = input("\nInput Current Admin Password: ")
    grant = accounts(username, password)
    #This makes sure the admins username and password matches with the already made code
    account = open(r"C:\database logs\accounts.txt", "a")
    if newpass == conpassword and grant:
    #This makes sure the passwords match and the admin is approved the account
        tbs = "\n" + newuser + "," + newpass
        account.write(str(tbs))
        incoming = "newuser"
        hold = tbs
        webRecord(incoming, hold)
        print("\nDone!")
    else:
        print("\nIncorrect admin login or not matching passwords.\n")

if __name__ == '__main__':
        main()