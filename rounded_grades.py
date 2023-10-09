# File name: rounded_grades.py
# Author: Bertram Hage, Johannes Nielsen
# Date: January 19, 2023
# Description: Contains a function that rounds grades to the nearest grade on the 7-step grade scale

from load_data import*

def rounded_grades(grades):
    #Takes a vector of grades and round them to the
    #nearest grade on the 7-step grade scale
    #Returns a vector with the rounded grades
    
    gradesRounded = []
    grades_7_step = [-3, 0, 2, 4, 7, 10, 12]
    
    for i in range(len(grades)):    
        closest_grade = min(grades_7_step, key=lambda x: abs(x - grades[i]))
        gradesRounded.append(closest_grade)
    
    return gradesRounded