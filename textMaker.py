'''
Created on Feb 26, 2021

@author: EMurphy24
'''
def main():
    name = input("What would you like your text document to be named?: ")
    name = name + ".txt"
    fhand = open(name, "w+")
    while True:
        mod == "1"
        modify(int(mod)) = input("What would you like the text document to say?")
        modify(int(mod)) = modify(int(mod)) + "\n"
        fhand = open(name, "w")
        fhand.write(modify(int(mod)))
        mod = int(mod)
        mod = mod + 1
        mod = str(mod) 
        cont = input("Add another line? (y,n): ")
        if cont ==  "y": continue
        else:
            fhand.close()
            print("Goodbye!")
            break
if __name__ == '__main__':
    main()