'''
Created on Oct 12, 2020

Version 1.0

Exersise 1&2, 2 is just an updated 1

No found bugs

@author: EMurphy24
'''
from _ast import Break #allows breaks
def main():
    while True:
        inp_p = input('Please put hours worked here') 
        inp_r = input('Please put your rate here')
        try: 
            hrs = int(inp_p) #converts hours string to float
            rate = int(inp_r)#Converts rate string into float
            pay = (hrs * rate) #does math to get rate
            print(pay)
        except: #If input cant be converted to float
            print("Please enter numbers in numerical terms.")
            continue #brings back to top of loop
if __name__ == '__main__':
    main()