'''
Created on March 3, 2021

@author: EMurphy24
'''


def main():
    
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
            
                
                
if __name__ == '__main__':
    main()