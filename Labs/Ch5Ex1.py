'''
Created on Nov 3, 2020

@author: EMurphy24
'''

def main():
    count = 0.0
    total = 0.0
    print("Welcome to the Number Counter 1.0. Please input 1 number at every input and type done when you are finished.\n")
    while True:
        try:
            ask = input("enter a number:")
            if ask == "done":
                average = total / count
                print("Total: " + str(total) + ", Count: " + str(count) + ", Average: " + str(average))
                count = 0.0
                total = 0.0
            elif ask.isnumeric():
                total = total + float(ask)
                count = count + 1        
        except:
            print("Please input a whole number")
            continue
        
if __name__ == '__main__':
    main()