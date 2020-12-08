'''
Created on Oct 27, 2020

Log: Oct 28: Added score system for normal version and added a rig function
     Oct 29: Added sound effects for point milestones and updated point system
     Nov 12: Added multiplayer feature, reorganized using less "if/else" to functions
     Nov 13: Fixed single player point bug

Bugs: Single player point errors *fixed*

Bonus: Rigged function, Multiplayer function, Game determines who wins on singleplayer, User has option to play again

@author: EMurphy24
'''

from random import randint
import random
import webbrowser
point = 0                                                                                                   #Creates point variable
def main():
    while True:           
        print("Welcome to Rock Paper Scissors: Python Edition. Follow the prompts and have fun!\n\n")
        y_nm = input("Would you like to play Rock Paper Scissors: ")
        print("\n")
        #Gives a extra line to make it look nicer
        if y_nm == "yes":
            s_m = input("Want to play single player or multiplayer? s / m:")
            print("\n")
            if s_m == "s": #I like to see this as a train station. Directs the computer where to run.
                sp() #singleplayer function
            elif s_m == "m":
                mp() #multiplayer function
            elif s_m == "r":
                rig() #rigged function
            elif s_m == "here we go now":
                pog() #easter egg 
            else:
                print("Please input s or m")
        elif y_nm == "no":
            print("Goodbye")
            break
        else:
            print("Please input yes or no")
            
def sp():
    point = 0                                                                                  #If they do...
    while True:
        try:
            rps = float(input("Please input rock (1), paper, (2), or scissors (3): "))          #Gets rock, paper, or scissor from player
            print("\n")
            rps_c = randint(1,3)                                                                #Gets a random number 1-3 to signify r, p, or s
            if rps == 1 and rps_c == 1:                                                         #Compares both answers and gives an output, tie, win, or loss.
                print("Tie! The computer had rock. Score: " + str(point) + "\n")                #Tells player if they won with their score updated
            elif rps == 1 and rps_c == 2:
                point = point - 1                                                               #Add/subtracts points
                print("You lost! The computer had paper! Score: " + str(point) + "\n")
            elif rps == 1 and rps_c == 3:
                point = point + 1
                print("You Won! The computer had scissors Score: " + str(point) + "\n")
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
            elif rps >= 3:
                print("please input 1, 2, or 3\n")
            if point == 5:                                                                      #If you get a total of 5 points, it will open a crowd cheering sound effect
                print("Wow 5 in a row! Lucky!\n")
                webbrowser.open('https://www.youtube.com/watch?v=barWV7RWkq0')
            elif point == -5:                                                                   #If you get a total of -5 points, it will open a sad trombone sound effect
                print("Somebody's having a bad day huh.\n")
                webbrowser.open('https://www.youtube.com/watch?v=yJxCdh1Ps48')
        except:
            print("Please input either 1, 2, or 3.\n")                                          #In case of a float greater the 3, it will give this error.                                                        
        

def mp():
        p1s = 0
        p2s = 0
        y_n = input("Do you want to play Rock, Paper, Scissors? Type y or n:")
        print("\n")                                                                                               
        if y_n == "y":                                                                                 
            while True:
                try:
                    rps = float(input("Player 1: Please input rock (1), paper, (2), or scissors (3): "))
                    #asks player 1 for input
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  
                    #hides player 1's answer        
                    rps_2 = float(input("Player 2: Please input rock (1), paper, (2), or scissors (3): "))
                    #asks player 2 for answer        
                    if rps == 1 and rps_2 == 1:                 
                        #Rock Vs Rock                                                  
                        print("Tie! You both chose had rock.\n")
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                        #announces score of players                
                    elif rps == 1 and rps_2 == 2:                                                               
                        print("Player 1 lost! Player 2 chose paper! had paper!\n")
                        p1s = p1s - 1
                        p2s = p2s + 1
                        #lines 102 
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 1 and rps_2 == 3:
                        print("Player 1 Won! Player 2 had scissors.\n")
                        p1s = p1s + 1
                        p2s = p2s - 1
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 2 and rps_2 == 1:
                        print("Player 1 Won! Player 2 had rock.\n")
                        p1s = p1s + 1
                        p2s = p2s - 1
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 2 and rps_2 == 2:
                        print("Tie! You both chose paper.\n")
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 2 and rps_2 == 3:
                        print("Player 1 lost! Player 2 had scissors.\n")
                        p1s = p1s - 1
                        p2s = p2s + 1
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 3 and rps_2 == 1:
                        print("Player 1 Lost! Player 2 had rock.\n")
                        p1s = p1s - 1
                        p2s = p2s + 1
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 3 and rps_2 == 2:
                        print("Player 1 won! Player 2 had paper.\n")
                        p1s = p1s + 1
                        p2s = p2s - 1
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps == 3 and rps_2 == 3:
                        print("Tie! You Both had scissors.\n")
                        print("Player 1 score: " + str(p1s) + ". Player 2 score: " + str(p2s))
                    elif rps >= 3:
                        print("Please input 1, 2, or 3\n")
                except:
                    print("Please input either 1, 2, or 3.\n")                                          
        elif y_n == "n":
            print("Goodbye!")
        else:
            print("Please input n or y\n") 
def rig():
    while True:
        try:
            rps = float(input("Please input rock (1), paper, (2), or scissors (3): "))                                                    
            if rps == 1:
                insultRock = ("You chose rock? What a fool. I chose paper.\n", "Oh come on, really? Too easy. I chose paper.\n", "This is pathetic. Are you even trying? I chose paper.\n")
                print(random.choice(insultRock))
                #randomly chooses one of the 3 insults in the list above
            elif rps == 2:
                insultPaper = ("Wow seriously? I've never played rock paper scissors with a more foolish player. I chose scissors.\n", "I expect better from you. Im not even trying. I chose scissors.\n", "I cant believe how little you try for this game. I chose scissors.\n")
                print(random.choice(insultPaper))
                #randomly chooses one of the 3 insults in the list above
            elif rps == 3:
                insultScissor = ("Seriously?!? Alright try this time alright? I got rock.\n", "Pathetic. Just pathetic. I got rock.\n", "My grandmother can do better then you. I got rock\n")
                print(random.choice(insultScissor))
                #randomly chooses one of the 3 insults in the list above
        except:
            print("Please input either 1, 2, or 3.\n")
def pog():
    webbrowser.open('https://www.youtube.com/watch?v=5VoUyGaV3TA') #easter egg
if __name__ == '__main__':
    main()