point = 0  
from random import randint
import webbrowser
def sp():
    point = 0
    y_n = input("Do you want to play Rock, Paper, Scissors? Type y or n:")                          #Asks player if they want to play?
    if y_n == "y":                                                                                  #If they do...
        while True:
            #try:
                rps = int(input("Please input rock (1), paper, (2), or scissors (3): "))          #Gets rock, paper, or scissor from player
                rps_c = randint(1,3)                                                                #Gets a random number 1-3 to signify r, p, or s
                if rps == 1 and rps_c == 1:                                                         #Compares both answers and gives an output, tie, win, or loss.
                    print("Tie! The computer had rock. Score: " + str(point) + "\n")                #Tells player if they won with their score updated
                elif rps == 1 and rps_c == 2:
                    point = point - 1                                                               #Add/subtracts points
                    print("You lost! The computer had paper! Score: " + str(point) + "\n")
                elif rps == 1 and rps_c == 3:
                    point = point + 1
                    print("You Won! The computer had scissors. Score: " + str(point) + "\n")
                elif rps == 2 and rps_c == 1:
                    point = point + 1
                    print("You Won! The computer had rock. Score: " + str(point) + "\n")
                elif rps == 2 and rps_c == 2:
                    print("Tie! The computer had paper. Score: " + str(point) + "\n")
                elif rps == 2 and rps_c == 3:
                    point = point - 1
                    print("You Lost! The computer had scissors. Score: " + str(point) + "\n")
                elif rps == 3 and rps_c == 1:
                    point = point - 1
                    print("You Lost! The computer had rock. Score: " + str(point) + "\n")
                elif rps == 3 and rps_c == 2:
                    point = point + 1
                    print("You won! The computer had paper. Score: " + str(point) + "\n")
                elif rps == 3 and rps_c == 3:
                    print("Tie! The computer had scissors. Score: " + str(point) + "\n")
                else:
                    print("broke")
                if point == 5:                                                                      #If you get a total of 5 points, it will open a crowd cheering sound effect
                    print("Wow 5 in a row! Lucky!\n")
                    webbrowser.open('https://www.youtube.com/watch?v=barWV7RWkq0')
                elif point == -5:                                                                   #If you get a total of -5 points, it will open a sad trombone sound effect
                    print("Somebody's having a bad day huh.\n")
                    webbrowser.open('https://www.youtube.com/watch?v=yJxCdh1Ps48')
            #except:
                #print("Please input either 1, 2, or 3.\n")                                          #In case of a float greater the 3, it will give this error.
    #elif y_n == "n":
        #print("Goodbye!")                                                                           #If they say n to if they want to play                 
    #else:
        #print("Please input n or y\n")    
        

if __name__ == '__main__':
    sp()