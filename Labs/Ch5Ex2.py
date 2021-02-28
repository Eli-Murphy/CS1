'''
Created on Nov 3, 2020

@author: EMurphy24
'''

def main():
    count = 0
    total = 0
    number_list = []
    print("Welcome to the Number Counter 2.0. Please input 1 number at every input and type done when you are finished.\n")
    while True:
        try:
            ask = input("enter a number:")
            ask = ask.lower()
            if ask == "done":
                print("Total: " + str(total) + ", Count: " + str(count) + ", Greatest: " + str(max(number_list)) + ", Smallest: " + str(min(number_list)))
                count = 0
                total = 0
                number_list = []
            elif ask.isdigit():
                total = total + int(ask)
                count = count + 1
                number_list.append(str(ask))
                print(number_list)
            elif ask == "end":
                print("Goodbye!")
                break
            else:
                print("Please input a number.\n")     
        except:
            print("Please input a number")
            continue
        
if __name__ == '__main__':
    main()