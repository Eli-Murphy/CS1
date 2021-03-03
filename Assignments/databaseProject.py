'''
Created on March 3, 2021

@author: EMurphy24
'''

def main():
    print("Welcome to the GCDS Directory")
    print("If you would like to search for info on somebody, enter 'search'.")
    goto = input("Enter Here: ")
    goto == goto.lower()
    if goto == "search":
        search()

def search():
    
    file_in = open('datatext.txt')
    first_name = input("Whats the first name of the person you are looking for?")
    first_name = first_name.lower()
    
    for line in file_in:
        line = line.lower()
        line = line.strip()
        listofwords = line.split(",  ")
        for word in listofwords:
            if word.startswith(first_name):
                print(line)
            else:
                break
            
#def isolate():


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
