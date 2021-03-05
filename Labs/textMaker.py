'''
Created on Feb 26, 2021

@author: EMurphy24
'''
def main():
    fhand = input('What is the file path?')
    selectedWord = input("What word would you like to isolate?: ")
    count = 0
    lcount = 0
    for line in fhand:
        lcount = lcount + 1
        line = line.rstrip()
        if selectedWord in line: 
            wordperline = int(line.count(selectedWord))
            count = count + wordperline
    print("Your file says ", selectedWord, str(count), " times.")
    print("Line count: ", str(lcount))


if __name__ == '__main__':
    
    main()