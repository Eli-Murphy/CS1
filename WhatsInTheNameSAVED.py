'''
Created on Jan 8, 2021

Logs: January 13th: Added 6 functions, 1,2,4,5,6,7 (3 has made me stumped)
                    Functions include flip(), vowelconst(), UL(), palindrome(), mixup(), split()\
      January 14th: Added Hyphen checker
      January 21st: Added name checker to deny future errors
      January 22nd: Seperated functions that were merged 
      January 27th: Added function documentation
                    Added 

Bugs: Symbols error, variable 'name' seems to not exist 

Initiative: Modifies your name in multiple ways, using functions made by me.

Bonus: Main Menu (main()), assorted array of characters (mixup())

@author: EMurphy24
'''


import random

def menu(word):
      
    '''
    This function is the main menu directing the user to the chosen functions
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  void, unless error, in which case str
    :raises: 
    '''
    
    print("\nMain Menu options:")
    print("For flipping your name press '1'")
    print("For the counting of vowels press '2'")
    print("For the counting of consonants press '3'")
    print("For the counting of spaces press '4'")
    print("For Hyphen checking, press '5'")
    print("For changing to upper case, press '6'")
    print("For changing to lower case, press 7")
    print("For palindrome testing, press '8'")
    print("For scrambling your name, press '9'")
    print("For selecting the first name, press '10'")
    print("For selecting the middle name, press '11'")
    print("For selecting the last name, press '12'\n")
    whereto = input("Input here: ")
    if whereto == "1":
        flip(word)                                  
    elif whereto == "2":
        vowel_count(word)                           
    elif whereto == "3":
        consonant_count(word)
    elif whereto == "4":
        space_count(word)
    elif whereto == "5":
        hyphen(word)                                
    elif whereto == "6":
        upper_case(word)                            
    elif whereto == "7":
        lower_case(word)                            
    elif whereto == "8":
        palindrome(word)                            
    elif whereto =="9":
        mixup(word)                                 
    elif whereto == "10":
        split_f(word)                                
    elif whereto == "11":
        split_m(word)                                
    elif whereto == "12":
        split_l(word)                                
    else:
        print("Please input 1-10")
        menu()
        
        
def flip(word):
    
    '''
    This function is designed to flip the word inputed
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    name_flip = word[::-1]                          #reverses order of index
    print("Your name backwards is " + name_flip)
    main()
    
def vowel_count(word):
    
    '''
    This function is designed to count and tell the user the amount of vowels in the name
 
    :param name: user input word
    :type name: string
    :type state: bool
    :returns: bool
    :raises: 
    '''

    count = 0
    for index in range(len(word)):              #Loop that runs the length of the input    
        if word[index] == 'a' or word[index] =='e' or word[index] =='i' or word[index] =='o' or word[index] =='u' or word[index] == 'A' or word[index] =='E' or word[index] =='I' or word[index] =='O' or word[index] =='U':
                                                #Line above checks if the index is a vowel
            count = count + 1                   #counts how many vowels
    print("You have " + str(count) + " vowels in your name.")
    
    
def consonant_count(word):
    
    '''
    This function is designed to count and tell the user the amount of consonants in the name
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  print function with str(int)
    :raises: 
    '''
    
    count = 0
    for index in range(len(word)):
            if word[index] != 'a' and word[index] !='e' and word[index] !='i' and word[index] !='o' and word[index] != 'u' and word[index] != 'A' and word[index] !='E' and word[index] != 'I' and word[index] !='O' and word[index] !='U':
                                                    #Line above checks if the index is not a vowel
                count += 1                          #adds to constant count point
    print("You have " + str(count) + " consonants in your name.")


def space_count(word):
    
    '''
    This function is designed to count and tell the user the amount of spaces in the name
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  print function with str(int)
    :raises: 
    '''
    
    count = 0
    for index in range(len(word)):
            if word[index] == ' ':                  #checks if the index is a space
                space_count += 1                    #adds to space count point
    print("You have " + count + " spaces in your name.")

def hyphen_f(word):
    '''
    This function is a formula to see if the input has a hyphen (-).
 
    :param name: user input word
    :type name: string
    :type state: bool
    :returns:  print function with str(int)
    :raises: 
    '''
    if "-" in word:                                 #Checks hyphen
        return True                                 #Sets ans of the function to be either T or F
    return False
        
def hyphen(word):
    
    '''
    This function is the printing function of hyphen_f()
 
    :param name: hyphen_f() bool
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    ans = hyphen_f(word)                            #Ans is the boolean result of hyphenF()
    
    if (ans):
        print("\nYes\n")
    else:
        print("\nNo\n")
            

def upper_case(word):
    
    '''
    This function is designed to capitalize the entire input using decimal values
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
        
    #VARIABLES
    letter_num=0
    output = ""
    
    for index in range(len(word)):                  #Loop that runs the length of the input
        letter = word[index]                        #gets letter from word
        letter_num = ord(letter)                    #converts to decimal from a ASCII table
        if letter_num >= 97 and letter_num <= 122:  #checks to see if the decimal is between 97 and 122 (lower case)
            letter_num = letter_num - 32            #switches it to upper case
        letter = chr(letter_num)                    #switches letter into the new format
        output = output + str(letter)               #appends the output by adding the letter
    print(output)
    
    
def lower_case(word): 
    
    '''
    This function is designed to "decapitalize" the entire input using decimal values
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    #VARIABLES
    letter_num=0
    output = ""
    
    for index in range(len(word)):                  #Loop that runs the length of the input
        letter = word[index]                        #gets letter from word
        letter_num = ord(letter)                    #converts to decimal from a ASCII table
        if letter_num >= 65 and letter_num <= 90:   #checks to see if the decimal is between 65 and 90 (upper case)
            letter_num = letter_num + 32            #switches it to lower case
        letter = chr(letter_num)                    #switches decimal into the letter
        output = output + str(letter)               #appends the output by adding the letter
    print(output)             


def is_palindrome_f(word):                                 
    
    '''
    This function is the formula for is_palandrome()
 
    :param name: user input word
    :type name: bool
    :type state: void
    :returns:  bool
    :raises: 
    '''
    
    for index in range(0, int(len(word)/2)):             #Runs loop for half of the length of the input 
        if word[index] != word[len(word)-index-1]:         #if half of the string's index is not half of the index backwards,
            return False
    return True
 
def palindrome(word):
    
    '''
    This function is designed to test if the word is a palindrome
 
    :param name: bool
    :type name: str
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    ans = is_palindrome_f(word)                           #runs IsPalindromeF() to see if true
 
    if (ans):
        print("\nYes, your name is a palindrome!\n")
    else:
        print("\nNo, your name is not a palindrome.\n")
        
        
        
def mixup(word):
    
    '''
    This function is designed scramble the word the user had input
 
    :param name: user input word
    :type name: str
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    wordlist = list(word)                               #Converts input to list
    newword = []                                        #Blank list to be filled
    for index in range(len(word)):                      #for however many characters are in the name
        letter = random.choice(wordlist)                #creates a temporary variable to hold the a random character
        newword.append(letter)                          #Puts that random character into a new list
        wordlist.remove(letter)                         #removes that character from being chosen again
        newword_str = ''.join(newword)                  #converts list to string
    print("\nYour new name is " + newword_str + ".\n")
    
    
def split_f(word):
    
    '''
    This function is designed to isolate the first word of the users input
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    split_word = []                                     #list that holds the new word
    placeholder  = ''                                   #empty variabe to remove spaces
    for words in word:                                  #Runs the loop for the amount of words there are in the input
        if words == ' ': 
            split_word.append(placeholder)              #removes spaces and replaces it with nothing
            placeholder = ''
        else:
            placeholder += words                        #adds spaceless word into list
    try:
        print(split_word[0])                            #grabs first part of the list and prints it
    except:
        print("Error: input was not 3 words. Restarting code for new input...\n")
        main()
        

def split_m(word):
    
    '''
    This function is designed to isolate the second word of the users input
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    split_word = []                                     #list that holds the new word
    placeholder  = ''                                   #empty variabe to remove spaces
    for words in word:                                  #Runs the loop for the amount of words there are in the input
        if words == ' ': 
            split_word.append(placeholder)              #removes spaces and replaces it with nothing
            placeholder = ''
        else:
            placeholder += words                        #adds spaceless word into list
    print(split_word)
    try:
        print(split_word[1])                            #grabs second part of the list and prints it
    except:
        print("Error: input was not 3 words. Restarting code for new input...\n")
        main()
    
    
def split_l(word):
    
    '''
    This function is designed to isolate the first word of the users input
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  str
    :raises: 
    '''
    
    word = word + " "
    split_word = []                                     #list that holds the new word
    placeholder  = ''                                   #empty variabe to remove spaces
    for words in word:                                  #Runs the loop for the amount of words there are in the input
        if words == ' ': 
            split_word.append(placeholder)              #removes spaces and replaces it with nothing
            placeholder = ''
        else:
            placeholder += words                        #adds spaceless word into list
    try:
        print(split_word[2])                                #grabs third part of the list and prints it
    except:
        print("Error: input was not 3 words. Restarting code for new input...\n")
        main()
    
    


def main():      
     
    '''
    This function is designed make sure the user input is accurate and will not error future code.
 
    :param name: user input word
    :type name: string
    :type state: void
    :returns:  void
    :raises: 
    '''
    
    print("Welcome to the Name Modifier! Made by Eli Murphy\n") #Code starts here

    word = input("What is your name? (First, Middle, Last): ")
    while True:
        unwanted = True
        for index in range(len(word)):
            letter = word[index]
            letter_num = ord(letter)
            if letter_num >= 97 and letter_num <= 122 or letter_num >= 65 and letter_num <= 90 or letter_num == 32:
                unwanted = True
            else:
                print("\nPlease input a character through A-Z or a-z.\n")
                unwanted = False                                         
                break
        if unwanted == True:
            menu(word)
    
                
if __name__ == '__main__':
    main()