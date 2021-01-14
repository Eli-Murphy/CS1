'''
Created on Jan 8, 2021

Logs: January 13th: Added 6 functions, 1,2,4,5,6,7 (3 has made me stumped)
                    Functions include flip(), vowelconst(), UL(), palindrome(), mixup(), split()

Bugs: Dosent have global variable, numbers error 

Initiative: Modifies your name in multiple ways, using functions made by me.

Bonus: Main Menu (main()), assorted array of characters (mixup())

@author: EMurphy24
'''

import random

def main():
    while True:
        print("Main Menu options:")
        print("For flipping your name press '1'")
        print("For the counting of vowels and consonants press '2'")
        print("For Hyphen checking, press '3'")
        print("For changing capitalization, press '4'")
        print("For palindrome testing, press '5'")
        print("For scrambling your name, press '6'")
        print("For splitting your name, press '7'\n")
        whereto = input("Input here:")
        if whereto == "1":
            flip()          #goto flip()
        elif whereto == "2":
            vowelconst()    #goto vowelconst()
        elif whereto =="4":
            UL()            #goto UL()
        elif whereto == "5":
            palindrome()  #goto palindrome
        elif whereto =="6":
            mixup()         #goto mixup()
        elif whereto == "7":
            split()         #goto split()
        else:
            break
        
        
        
def flip():
    name_flip = word[::-1]                          #reverses order of index
    print("Your name backwards is " + name_flip)
    main()
    
    
def vowelconst():
    
    #VARIABLES
    space_count = 0
    vowel_count = 0
    constant_count = 0
    
    try:
        for index in range(len(word)):              #Loop that runs the length of the input
            if word[index] == 'a' or word[index] =='e' or word[index] =='i' or word[index] =='o' or word[index] =='u' or word[index] == 'A' or word[index] =='E' or word[index] =='I' or word[index] =='O' or word[index] =='U':
                                                    #Line above checks if the index is a vowel
                vowel_count += 1                    #adds to vowel count point 
        for index in range(len(word)):
            if word[index] != 'a' and word[index] !='e' and word[index] !='i' and word[index] !='o' and word[index] != 'u' and word[index] != 'A' and word[index] !='E' and word[index] != 'I' and word[index] !='O' and word[index] !='U':
                                                    #Line above checks if the index is not a vowel
                constant_count += 1                 #adds to constant count point
        for index in range(len(word)):
            if word[index] == ' ':                  #checks if the index is a space
                space_count += 1                    #adds to space count point
        print("There are " + str(vowel_count) + " vowels, " + str(constant_count) + " consonants, and " + str(space_count) + " spaces.")
                                                    #line above puts the counts together
        main()
    except:
        print("invalid input")
        vowelconst()
        
def hyphenF(word):
    if "-" in word:
        return True
    return False
        
def hyphen():
    ans = hyphenF(word)
    
    if (ans):
        print("Yes\n\n")
    else:
        print("No\n\n")
            

def UL():
    u_or_l = input("Would you like it in upper case (1) or lower case (2)? ")
    
    #VARIABLES
    letter_num=0
    output = ""
    
    if u_or_l == "1":
        for index in range(len(word)):                  #Loop that runs the length of the input
            letter = word[index]                        #gets letter from word
            letter_num = ord(letter)                    #converts to decimal from a ASCII table
            if letter_num >= 97 and letter_num <= 122:  #checks to see if the decimal is between 97 and 122 (lower case)
                letter_num = letter_num - 32            #switches it to upper case
            letter = chr(letter_num)                    #switches letter into the new format
            output = output + str(letter)               #appends the output by adding the letter
        print(output)
              
    elif u_or_l == "2":
        for index in range(len(word)):                  #see above documentation
            letter = word[index]
            letter_num = ord(letter)
            if letter_num >= 65 and letter_num <= 90:   #difference here is that it now checks to see if it is between 65 and 90 (upper case
                letter_num = letter_num + 32            
            letter = chr(letter_num)
            output = output + str(letter)
        print(output)
    else:
        print("Please input letters")
        UL()


def isPalindromeF(str):                                 #formula for palindrome
    for index in range(0, int(len(str)/2)):             #Runs loop for half of the length of the input 
        if str[index] != str[len(str)-index-1]:         #if half of the string's index is not half of the index backwards,
            return False
    return True
 
def palindrome():
    ans = isPalindromeF(word)                           #runs IsPalindromeF() to see if true
 
    if (ans):
        print("Yes\n\n")
    else:
        print("No\n\n")
def mixup():
    wordlist = list(word)
    newword = []
    for index in range(len(word)):
        letter = random.choice(wordlist)
        newword.append(letter)
        wordlist.remove(letter)
        newword_str = ''.join(newword)
    print(newword_str + "\n\n")
def split():
    place = input("What name would you like to isolate? First(1), Middle(2), Last(3): ")
    split_word = []
    placeholder  = ''
    for words in word:                                  #Runs the loop for the amount of words there are in the input
        if words == ' ': 
            split_word.append(placeholder) 
            placeholder = ''
        else:
            placeholder += words 
    if placeholder:
        split_word.append(placeholder)
    if place == "1":
        name = split_word[0]                            #grabs first word in list
    elif place == "2":
        name =split_word[1]                             #grabs second,
    elif place == "3":
        name =split_word[2]                             #and third
    else:
        print("Please input a three worded phrase or use dashes to signify multi-worded names. ex. Mary-Jane")
        split()
    print("Your isolated word is "+ name)
        
print("Welcome to the Name Modifier! Made by Eli Murphy\n")
word = input("What is your name? (First, Middle, Last): ")        
        
    
                
if __name__ == '__main__':
    main()