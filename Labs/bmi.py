'''
Created on Oct 22, 2020

Version 1.0

Bugs: None found

Calculates BMI using inches and 

@author: EMurphy24
'''
def main():
    print("Welcome to the BMI calculator")
    while True:
        try:
            inp_ft = input("Feet:")
            inp_in = input("Inches:")
            ft = float(inp_ft)                                  #converts to float for math
            inch = float(inp_in)
            inp_ht = (ft * 12) + inch                           #convert feet into inches, adds inches, then makes it the total height.
            inp2 = input("Weight in Lbs:") 
            ht = float(inp_ht)
            wt = float(inp2)
            form_fix = 703                                      #added to fix the coversion issue from imperial and standard
            formula = (wt / (ht * ht)) * form_fix               #calculate bmi
            if formula <= 18.5:
                bmi_round = round(formula, 1)                   #rounds formula to nearest tenth
                bmi = str(bmi_round)                            #converts rounded bmi into string
                print("Underweight with a BMI of:" + bmi)       #says your status and bmi
            elif formula >= 18.5 and formula <= 24.9:
                bmi_round = round(formula, 1)
                bmi = str(bmi_round)
                print("Normal Weight with a BMI of:" + bmi)
            elif formula >= 24.9 and formula <= 29.9:
                bmi_round = round(formula, 1)
                bmi = str(bmi_round)
                print("Overweight with a BMI of:" + bmi)
            else:
                bmi_round = round(formula, 1)
                bmi = str(bmi_round)
                print("Obese with a BMI of:" + bmi)
        except:
            print("Please input correct units")                #In case of poor input    

if __name__ == '__main__':
    main()