'''
Created on Jan 8, 2021

@author: EMurphy24
'''
def main():
    while True:
        word = input("Please input your desired word: ")
        
        #VARIABLES
        vowel_count = 0
        lower_count = 0
        upper_count = 0
        constant_count = 0
        space_count = 0
        
        
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
            for index in range(len(word)):
                letter = word[index]
                letter_num = ord(letter)
                letter = chr(letter_num)
                if letter_num >= 97 and letter_num <= 122:
                    lower_count += 1
                elif letter_num >= 65 and letter_num <= 90:
                    upper_count += 1
            constant_count = constant_count - space_count
            print("There are " + str(vowel_count) + " vowels, " + str(constant_count) + " consonants, and " + str(space_count) + " spaces.")
            print("There are " + str(upper_count) + " upper case letters and " + str(lower_count) + " lower case letters")
        except:
            print("Error")
                
            


if __name__ == '__main__':
    main()