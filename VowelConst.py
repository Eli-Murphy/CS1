'''
Created on Jan 8, 2021

@author: EMurphy24
'''
def main():
    while True:
        word = input("Please input your desired word: ")
        vowel_count = 0
        constant_count = 0
        space_count = 0
        try:
            for index in range(len(word)):
                if word[index] == 'a' or word[index] =='e' or word[index] =='i' or word[index] =='o' or word[index] =='u':
                    vowel_count += 1
            for index in range(len(word)):
                if word[index] != 'a' and word[index] !='e' and word[index] !='i' and word[index] !='o' and word[index] !='u':
                    constant_count += 1
            for index in range(len(word)):
                if word[index] == ' ':
                    space_count += 1
            constant_count = constant_count - space_count
            print("There are " + str(vowel_count) + " vowels, " + str(constant_count) + " consonants, and " + str(space_count) + " spaces.")
        except:
            print("Error")
                
            


if __name__ == '__main__':
    main()