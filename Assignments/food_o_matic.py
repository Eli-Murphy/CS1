'''
Created on November 16, 2020

Log: November 16th: Added Insults and menu maker, fully functional
     November 17th: Added baked good section. Added way so no same word is said twice in menu items and baking.
     November 18th: Added sudocode/comments and made notice of the maximum possibilities in ideas. 
     November 19th: Converts main menu to lower case so any main menu would work ("Main Menu", "mAin MeNu", "MAIN MENU")
                    Added price of menu items in food()

Bugs: No known bugs

Bonus: Change the domain (3 domains) , Allow multiple items from one list, wont show duplicate words in menu items and baked goods

@author: EMurphy24
'''

import random
def main():
    print("Welcome to Python Item Generator, created by Eli Murphy. Say 'main menu' at any input to return to the selection!\n\n")
    while True:
        itemmaker = input("What would you like to generate? Fancy Insults (1), Menu items (2), or baked good ideas (3): ")
        print("\n") #gives space
        if itemmaker == "1":
            insult()
        elif itemmaker == "2":
            food()
        elif itemmaker == "3":
            baking()
        elif itemmaker == "exit":
            print("Goodbye!")
            break
        else: 
            print("Please input either 1, 2 or 3.")
    #This section of the code is the directory and main menu for the user. 
    #Depending on the input of the question, it would bring the user to
    #the desired location through various functions.
            
    
def food():
    print("***Note: Due to the nature of the program to remove duplicate ideas, it deletes possibilitys, making errors pop up if it runs out of menu items.\n")
    while True:
        try:
            times = input("\nHow many menu items would you like to generate: ")
            how = ["local", "roasted", "grilled", "garlic", "mashed", "oven dried", "spiced", "stewed", "assorted", "iced", "sliced", "braised", "free-range", "baby", "teriyaki glazed", "steamed"]
            food_price = ["9 for a head","5.51 per lb","4 per lb", "6 per can", "1.66 per lb", "1.25 per lb", "4 per lb", "6 per lb", "1 per lb", "1.50 per each", " 1.50 per lb", "4.50 per lb", "7 per lb", "3 per lb", "2 per lb"]
            food = ["cauliflower", "tilapia fish", "pork loin", "green beans", "basmati rice", "rainbow carrots", "fingerling potatos", "three color squash", "potatos", "eggplant", "drumstick", "shortrib", "duck breast", "eye round of beef", "baguette"]
            desc_side = ["with fennel", "gratin", "bengali style", "with peas", "pizza", "with balsamico", "with garlic and olive oil", "with piegon peas", "with minted yogurt", "soup", "chutney", "salad", "with tropical fruit salad", "over sticky rice", "au jus"]
            #These lists are full of possible options for the randomizer (below) to use.
            times = times.lower()
            if times == "main menu":
                print(" ")
                break
                #Brings the user back to main()
            elif times.isdigit():
                print(" ") 
                #This is do stop the else error I found.
            else:
                print(" ")
                #This fixes any unfriendly inputs and restarts from the loop.
            for x in range (0, int(times)):
                #This gives the code the ability to make the desired amount of items depending on the input
                twoorone = random.randint(1,2)
                if twoorone == 1:
                    item1 = random.choice(how)
                    item1_2 = random.choice(how)
                    #This is to get 2 different "how" items
                    item2_num = random.randint(0, len(food))
                    item2 = food[item2_num]
                    item2_price = food_price[item2_num]
                    #This calculates the matched price
                    
                    item3 = random.choice(desc_side)
                    
                    print("\n" + item1 + " " + item1_2 + " " + item2 + " " + item3)
                    #This line puts the variables together and gives the user the idea
                    print("The " + item2 + " will cost you $" + item2_price)
                    
                    food.remove(item2)
                    desc_side.remove(item3)
                    #This removes the type of food and side from the list to remove duplicates, but leaves "how"
                elif twoorone == 2:
                    item1 = random.choice(how)
                    item2 = random.choice(food)
                    item3 = random.choice(desc_side)
                    item2_num = random.randint(0, len(food))
                    item2 = food[item2_num]
                    item2_price = food_price[item2_num]
                    #This calculates the matched price
                    print("\n" + item1 + " " + item2 + " " + item3)
                    print("The " + item2 + " will cost you $" + item2_price)
                    how.remove(item1)
                    food.remove(item2)
                    desc_side.remove(item3)
                    #same situation here as above, but gives the user a 50/50 chance of having 1 or 2 "how" items
        except:
            print("Error. Either too many requests or invalid input")
            #Friendly error to overload or invalid input
def insult():
    #Code in this function is fairly similar besides the editing of lists, making infinite amount of possibilities.
    while True:
        try:
            times = input("How many insults would you like to generate: ")
            i1=["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning", "fobbing", "forward", "frothy", "gleeking", "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "paunchy", "pribbling", "puking", "puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering", "unmuzzled", "vain", "venomed", "villainous", "warped", "wayward", "weedy", "yeast"]
            i2=["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed", "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten"]
            i3=["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench", "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail"]
            #Lists created by TeachWithICT
            times = times.lower()
            if times == "main menu":
                break
            elif times.isdigit():
                print(" ")
            else:
                print(" ")
            for x in range (0, int(times)):
                print(random.choice(i1) + " " + random.choice(i2) + " " + random.choice(i3))
        except:
            print("Error. Either too many requests or invalid input")
            
def baking():
    
    #this function is identical to food() besides the name of variables and the fact that you cant have two types of idea.
    print("***Note: Due to the nature of the program to remove duplicate ideas, it deletes possibilitys, making errors pop up if it runs out of menu items.\n")
    while True:
        try:
            times = input("How many baked good ideas would you like to generate: ")
            flavor = ["Chocolate","Vanilla","Orange","pecan","Lemon","watermelon","Rum","Blueberry","raspberry","Key Lime","pumpkin","apple","pecan","sweet potato","oreo","pistachio","banana","strawberry","coconut","pineapple"]
            base = ["Cake","pie","cupcakes","brulle","cookies","ice cream","pudding","tart","crumble","croissant","bar","bread","muffin","popsicle"]
            garnish = ["with chocolate chips","with mint", "with peppermint","with butterscotch","with carmamel","with fudge","a la mode","with oreo", "with crushed pretzel", "with assorted berries","with white choclate","with crushed nuts","with granola"]
            times = times.lower()
            if times == "main menu":
                break
            elif times.isdigit():
                print(" ")
            else:
                print(" ")
            for x in range (0, int(times)):
                item1 = random.choice(flavor)
                item2 = random.choice(base)
                item3 = random.choice(garnish)
                print(item1 + " " + item2 + " " + item3)
                flavor.remove(item1)
                base.remove(item2)
                garnish.remove(item3)
        except:
            print("Error. Either too many requests or invalid input")

                
if __name__ == '__main__':
    main()