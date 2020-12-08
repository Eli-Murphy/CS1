'''
Created on Oct 13, 2020

@author: EMurphy24
'''
def main():
    import random
    head_or_tail = random.randint(0,1) #Head/Tail
    type = random.randint(0,3) #
    

    if head_or_tail == 0:
        print("heads")
    else:
        print("tails")
    if type == 0:
        print("penny")
    elif type == 1:
        print("Nickel")
    elif type == 2:
        print("dime")
    elif type == 3:
        print("quarter")
if __name__ == '__main__':
    main()