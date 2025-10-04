#HW4?-Yasser Daffa

#Second Try

import numpy as np


#----------logic----------#

#This function calculates the power dissipated on a resistor. where amp is the current flown. and ohm is the resistor.
def powerFunction(amp: float, ohm: float):
    power = amp**2 * ohm

    return power


#This function solves a system of two equations. where a, b, c, d, are the coeffiecients, and e, f are the constants
def solve_equationFunction(a:float, b:float, c:float, d:float, e:float, f:float):
    
    Coeffiecients = np.array([[a, b], [d, e]])
        #creates an array [a, b]
        #                 [d, e]
                                                            
    Constants = np.array([c, f])

    Solution = np.linalg.solve(Coeffiecients, Constants)

    #takes the solution in(first column and second column) and stores it in I1 and I2 respectively
    I1 = Solution[0]
    I2 = Solution[1]

    return I1, I2


#----------Execution Functions----------#


#This function runs the Power Dissipation function (powerFunction).
#It prompts the user to enter input as a string then checks whether the user entered "back"..
#if the input couldnt be turned into a float (due to the user entering invalid strings) the function returns error

def Run_powerFunction():
    print("--Welcome to power function-- \n *INFO: This function calculates power in watts.. From Current and Resistance*")
    while True:
        UserInput = input("To go back.. type 'back' \nEnter Current in Amps and Resistances in Ohm.. Separated by comma. e.g. '2, 15': ")
        try:
            if UserInput == "back".lower():
                print("- Going Backwards!! -")
                break
                            
            amp, ohm = eval(UserInput)

            print(f"The power dissipated is ",powerFunction(amp, ohm),"Watts")

        #checks if the user entered more than 2 digits
        #if so, it returns an error
        except ValueError:
            print("Please only enter numbers.. only 2 digits and no letters or symbols!")
            continue
        
        #checks if the user entered any letters or special characters
        #if so, it returns an error
        except Exception:
            print("ERROR! Please enter values as instructed (2 digits)!! or enter 'back' to go back")
            continue



#This function runs the Solve Equation fucntion (solve_equationFunction).
#It prompts the user to enter input as a string then checks whether the user entered "back"..
#if the input couldnt be turned into a float (due to the user entering invalid strings) the function returns error

def Run_solve_equationFunction():
    print("--Welcome to Two Equations function-- \n *INFO: This function solves system of two equations...*")
    while True:
        UserInput = input("To go back.. type 'back' \nEnter coeifficents for two equations. separated by comma (a,b,c, d,e,f) e.g. '10,5,15, 5,12,10': ")
        try:
            #Checks if input is 'back' the function quits the loop..
            if UserInput == "back".lower():
                print("- Going Backwards!! -")
                break
            
            #if input wasnt 'back' the function proceeds to check if it can split user input into 6 variables
            #if it wasnt able to split (due to user entering less than 6 digits or a string) the function continues to the except ValueError and returns an error.
            a,b,c,d,e,f = eval(UserInput)

            solution = solve_equationFunction(a,b,c,d,e,f)
            

            print(f"The answers are i1 = {solution[0]:.2f}A, i2 = {solution[1]:.2f}A")

        #checks if the user entered more or less than 6 digits
        #if so, it returns an error
        except ValueError:
            print("Please only enter numbers.. only 6 digits and no letters or symbols!")
            continue

        #checks if the user entered any letters or special characters
        #if so, it returns an error
        except Exception:
            print("ERROR! Please enter values as instructed!! or enter 'back' to go back")
            continue



#This is the main function that runs the program:
#it prompts the user to enter number between 1, 2, and 0. 
#Where if the user entered 0 or entered the word 'exit'.. the function quits the loop
#If the user entered 1, program runs the (Run_powerFunction)
#If the user entered 2, program runs the (Run_solveequationFunction)

def main():
    while True:
        print("----Main Menu----")
        try:
            userPick = input("Enter your choice 1 or 2 or type 'exit' or 0 to exit... \n 1. Calculate Power dissipation. \n 2. Solving Two system of equations. \n choice: ")

            if userPick == "exit".lower() or userPick == "0":
                print("exiting program ;-; ")
                break
            
            elif userPick == "1":
                Run_powerFunction()

            elif userPick == "2":
                Run_solve_equationFunction()
            
            else:
                print("ERROR!! Kindly enter values either 1, 2 or if you want to exit type 'exit' or 0...")

        except Exception:
            print("Error!! Try entering values again.")


#running the main function. (otherwise nothing would happen)
main()

