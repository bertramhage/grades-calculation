# File name: compute_final_grades.py
# Author: Bertram Hage, Johannes Nielsen
# Date: January 19, 2023
# Description: This script contains a function for computing the final grade of students.

import numpy as np
from load_data import*

def compute_final_grades(grades):
#Takes a matrix of grades
#Checks if the person got the grade -3 or only one grade
#else it deletes the lowest grade 
#and calculate the avarage grades  
#gives a vector as an output
    gradesFinal = np.array([])
    
    #chechs if there is only one grade
    if grades.shape[1] == 3:
        individuelGrade = grades.iloc[:,2]
        gradesFinal = np.append(gradesFinal, individuelGrade)
    else:
        for i in grades.index:
            #search for the grade -3
            if (grades.iloc[i,2:] == -3).any():
                individuelGrade = -3
                gradesFinal = np.append(gradesFinal, individuelGrade)
                
            else:
            #calculate final grade
                gradesOne = sum(grades.iloc[i,2:])-min(grades.iloc[i,2:])
                gradestwo = gradesOne/(grades.iloc[:,2:].shape[1]-1)
                gradesFinal = np.append(gradesFinal, gradestwo)
                    
    return gradesFinal
