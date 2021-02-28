'''
Created on Oct 12, 2020

Version 1.5

Bugs: Numbers above 1.0 will be considered a A.

Exercise 3
Calculates grade using decimals

@author: EMurphy24
'''
def main():
    while True:
        inp = input("Please input your grade from 1.0 to 0.0") #gets grade
        try:
            grade = float(inp)
            if grade >= 0.9:
                print("A, Nice job!") #a grade higher then a 90 will be an A
            elif grade >= 0.8:
                    print("B")
            elif grade >= 0.7:
                print("C")
            elif grade >= 0.6:
                print("D")
            elif grade < 0.6:
                print("F")
        except:
            print("Please enter a number from 1.0 - 0.0") #if input cant be converted to float
            continue
        
        

if __name__ == '__main__':
    main()