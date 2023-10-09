# File name: check_error.py
# Author: Bertram Hage, Johannes Nielsen
# Date: January 19, 2023
# Description: This script contains a function for checking errors in loaded data.

from load_data import*

def check_error(grades):
    #Takes a dataframe and checks it for the errors:
    #Duplicat IDs and invalid grades
    #Prints the errors to the user
    #Does not return anything

    duplicateIDs = []
    invalidGradesRows = []
    valid_values = [-3,0,2,4,7,10,12]
    
    for i in range(grades.shape[0]):
        
        #Check for duplicate IDs
        studentID = grades.iloc[i,0]
        count = grades.iloc[:,0][grades.iloc[:,0] == studentID].shape[0]
        
        if (count > 1) and not (studentID in duplicateIDs):
            duplicateIDs.append(studentID)
            
            
        #Check for invalid grades
        if not (grades.iloc[i,2:].isin(valid_values).all()):
            invalidGradesRows.append(i+1)
    
    #Print info regarding duplicate IDs
    for value in duplicateIDs:
        duplicateIDRows = grades.iloc[:,0][grades.iloc[:,0] == value].index+1
        print("The ID {:s} appear {:d} times, at line ".format(value, len(duplicateIDRows)) + ",".join(str(e) for e in duplicateIDRows))
    
    #Print info regarding invalid grades
    if len(invalidGradesRows) > 0:
        print("Invalid grades on line " + ", ".join(str(e) for e in invalidGradesRows))
        print("") #Line break
    
    #If no errors were found
    if (len(duplicateIDs) == 0) and (len(invalidGradesRows) == 0):
        print("No errors in table")
        print("") #Line break
