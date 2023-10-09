# File name: main_script.py
# Author: Bertram Hage, Johannes Nielsen
# Date: January 19, 2023
# Description: Main script containing main loop for program execution.

import os
import numpy as np

from load_data import*
from rounded_grades import*
from compute_final_grades import*
from grades_plot import*
from check_error import*


def inputNumber(prompt):
    #Function for checking whether menu input is valid
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("Input not valid")
            pass
    return num

def displayMenu(options):
    #Function for displaying menu and saving selected option
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))

    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose one of the menu item: ")
        print("") #Line break
    return choice

options = ['Load new data', 'Check for data errors', 'Generate plots', 'Display list of grades', 'Quit']

#### Program ####

#Initialization
print("\n################################################")
print("### Welcome to Program for grading students! ###")
print("################################################\n")


#Load data
while True:
     filename = input("Input the filename of a data file: ")

     if filename == "list":
         print(os.listdir())
         continue

     try:
         data = load_data(filename)
         break

     except:
         print("File {:s} not in directory.".format(filename))
         print('Write "list" to show available files.')
         print("") #Line break
         pass

#Data information
print("\n####Data loaded successfully####\n")

print("Data contains {:d} students and {:d} assignments\n".format(data.shape[0], data.shape[1]-2))

check_error(data)

#Main loop
while True:
    
    choice = displayMenu(options)

    if choice == 5:
        break

    else:
        if choice == 1: #Load new data
            while True:
                filename = input("Input the filename of a data file: ")

                if filename == "list":
                    print(os.listdir())
                    continue

                try:
                    data = load_data(filename)
                    break
        
                except:
                    print("File {:s} not in directory.".format(filename))
                    print('Write "list" to show available files.\n')
                    pass

            print("\n####Data loaded successfully####\n")
            print("Data contains {:d} students and {:d} assignments\n".format(data.shape[0], data.shape[1]-2))

        elif choice == 2: #Check for data errors
            try:
                check_error(data)
            except NameError:
                print("####No data loaded. Input data first.####\n")
                continue
                
        elif choice == 3: #Generate plots
            try:
                grades_plot(data)
            except NameError:
                print("####No data loaded. Input data first.####\n")
                continue
            
        elif choice == 4: #Display list of grades
            try:
                finalGrades = compute_final_grades(data)
                finalGrades = rounded_grades(finalGrades) #Round grades to 7-scale
                listOfGrades = data.copy()
                listOfGrades['Final Grade'] = finalGrades
                sortedListOfGrades = listOfGrades.sort_values(by="Name")
                print(sortedListOfGrades)
                print('') #Line break
            except NameError:
                print("####No data loaded. Input data first.####\n")
            
                continue