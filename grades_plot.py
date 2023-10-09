# File name: grades_plot.py
# Author: Bertram Hage, Johannes Nielsen
# Date: January 19, 2023
# Description: This script contains a function for producing relevant figures describing the distribution of grades.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from compute_final_grades import *
from rounded_grades import *

def grades_plot(grades):
    #Takes a dataframe containing the grades and 
    #creates two plots:
    #"Final grades" - a bar plot showing grade distribution
    #"Grades per assignment" - a plot showing assignment grades
    #Does not return anything
    
    #Get final grades
    finalGrades = compute_final_grades(grades)
    
    #Round final grades
    finalGrades = np.array(rounded_grades(finalGrades))
   
    #Frequency of each final grade -3, 0, ..., 12
    gradeFrequency = []
   
    #Create figure containing two plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    #Calculate frequency of grades
    for grade in [-3,0,2,4,7,10,12]:
        freq = len(finalGrades[finalGrades == grade])
        gradeFrequency.append(freq)
    
    #Create matrix containing assignment number and grades from dataframe
    assignmentGrades = grades.iloc[:,2:].to_numpy().T

    #Create x- and y-values for "Grades per assignment"-plot
    xvals = []
    yvals = []
    for i in range(assignmentGrades.shape[0]):
        new_values = [i+1]*assignmentGrades.shape[1]
        new_values = new_values + np.arange(-0.1, 0.1, (0.2/len(new_values)))
        xvals.extend(new_values)
        yvals.extend(assignmentGrades[i,:].tolist())
    
    #Create average grades per assignment plot line
    avgXvals = []
    avgYvals = []
    for i in range(assignmentGrades.shape[0]):
        avgXvals.append(i+0.5)
        avgXvals.append(i+1.5)
        avgYvals.append(sum(assignmentGrades[i,:])/len(assignmentGrades[i,:]))
        avgYvals.append(sum(assignmentGrades[i,:])/len(assignmentGrades[i,:]))

    #Make bar plot "Final Grades"
    ax1.bar([-3,0,2,4,7,10,12], gradeFrequency)
    ax1.set_title("Final grades")
    ax1.set_xlabel("Grade")
    ax1.set_ylabel("Frequency")
    ax1.set_xticks([-3, 0, 2, 4, 7, 10, 12])
    
    #Make plot "Grades per assignment"
    ax2.plot(xvals, yvals, "bo", markersize=4)
    ax2.set_yticks([-3, 0, 2, 4, 7, 10, 12])
    ax2.plot(avgXvals, avgYvals, 'r-')
    ax2.set_title("Grades per assignment")
    ax2.set_xlabel("Assignment #")
    ax2.set_ylabel("Grades")
    ax2.legend(["Grades", "Average grades"])

    #Show both plots
    plt.show()