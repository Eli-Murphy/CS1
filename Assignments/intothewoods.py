'''
Created on Feb 26, 2021

@author: EMurphy24
'''
def main():
    fhand = open('intothewoods.txt')
    selectedWord = input("What word would you like to isolate?: ")
    count = 0
    lcount = 0
    for line in fhand:
        lcount = lcount + 1
        line = line.rstrip()
        if selectedWord in line: 
            wordperline = int(line.count(selectedWord))
            count = count + wordperline
    print("Into The Woods has", str(count), "of your selected word.")
    print("Line count: ", lcount)
    

if __name__ == '__main__':
    main()