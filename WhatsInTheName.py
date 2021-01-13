'''
Created on Jan 8, 2021

@author: EMurphy24
'''

#word = ""
import random

def main():
    print("Welcome to the Name Modifier! Made by Eli Murphy\n")
    #word = input("Before we begin, what is the name you will be modifying? ")
    while True:
        print("Main Menu options:")
        print("For flipping your name press '1'")
        print("For the counting of vowels and consonants press '2'")
        print("For changing capitalization, press '4'")
        print("For palindrome testing, press '5'")
        whereto = input("Input here:")
        if whereto == "1":
            flip() #goto flip()
        elif whereto == "2":
            vowelconst() #goto vowelconst()
        elif whereto =="4":
            UL() #goto UL()
        elif whereto == "5":
            isPalindrome() #goto isPalindrome
        elif whereto =="6":
            mixup()
        else:
            break
        
        
        
def flip():
    word= input("What is your name (First Middle Last): ")
    name_flip = word[::-1]
    print("Your name backwards is " + name_flip)
    main()
    
    
def vowelconst():
    word = input("What is your name (First Middle Last): ")
    
    #VARIABLES
    space_count = 0
    vowel_count = 0
    constant_count = 0
    
    try:
        for index in range(len(word)):
            if word[index] == 'a' or word[index] =='e' or word[index] =='i' or word[index] =='o' or word[index] =='u' or word[index] == 'A' or word[index] =='E' or word[index] =='I' or word[index] =='O' or word[index] =='U':
                vowel_count += 1
        for index in range(len(word)):
            if word[index] != 'a' and word[index] !='e' and word[index] !='i' and word[index] !='o' and word[index] != 'u' and word[index] != 'A' and word[index] !='E' and word[index] != 'I' and word[index] !='O' and word[index] !='U':
                constant_count += 1
        for index in range(len(word)):
            if word[index] == ' ':
                space_count += 1
        print("There are " + str(vowel_count) + " vowels, " + str(constant_count) + " consonants, and " + str(space_count) + " spaces.")
        main()
    except:
        print("invalid input")
        vowelconst()
        
        

def UL():
    word = input("What is your name (First Middle Last): ")
    u_or_l = input("Would you like it in upper case (1), lower case (2), or flipped (3)? ")
    
    #VARIABLES
    letter_num=0
    output = ""
    
    if u_or_l == "1":
        for index in range(len(word)):
            letter = word[index]
            letter_num = ord(letter)
            #print("62", letter_num)
            #letter = chr(letter_num)
            if letter_num >= 97 and letter_num <= 122:
                letter_num = letter_num - 32
                #print("66", letter_num)
            letter = chr(letter_num)
            output = output + str(letter)
        print(output)
              
    elif u_or_l == "2":
        for index in range(len(word)):
            letter = word[index]
            letter_num = ord(letter)
            #print("62", letter_num)
            #letter = chr(letter_num)
            if letter_num >= 65 and letter_num <= 90:
                letter_num = letter_num + 32
                #print("66", letter_num)
            letter = chr(letter_num)
            output = output + str(letter)
        print(output)
    else:
        print("Please input letters")
        UL()


def isPalindromeF(str):
 
     
    for index in range(0, int(len(str)/2)): #Runs loop for half of the length of the input 
        if str[index] != str[len(str)-index-1]: # if half of the string's index is not half of the index backwards,
            return False
    return True
 
def isPalindrome():
    word = input("What is your name (First Middle Last): ")
    ans = isPalindromeF(word) #runs IsPalindromeF() to see if true
 
    if (ans):
        print("Yes\n\n")
    else:
        print("No\n\n")
def mixup():
    word = input("What is your name (First Middle Last): ")
    wordlist = list(word)
    newword = []
    for index in range(len(word)):
        letter = random.choice(wordlist)
        newword.append(letter)
        wordlist.remove(letter)
        newword_str = ''.join(newword)
    print(newword_str + "\n\n")
        
        
    
                
if __name__ == '__main__':
    main()