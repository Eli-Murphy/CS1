'''
Created on Feb 26, 2021

@author: EMurphy24
'''
def main():
    fhand = open('intothewoods.txt')
    for line in fhand:
        line = line.rstrip()
        if line.find('woods') == -1: continue
        print(line)
    

if __name__ == '__main__':
    main()