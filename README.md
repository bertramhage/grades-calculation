# Student Grades Analysis Program

A introductory python script for generating statistics and computing of final grades over multiple assignments. As part of the course Introduction to programming and data processing. 

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Load Data**: Load student data from a CSV file.
- **Check for Data Errors**: Detect and report errors in the loaded data, such as duplicate IDs or invalid grades.
- **Generate Plots**: Create plots to visualize grade distributions and grades per assignment.
- **Display List of Grades**: Display a list of student names and their final grades.

## Usage

1. **Load Data**:
   - Run `main_script.py` and choose the option to load new data.
   - Enter the filename of the data file in CSV format located in the program folder or path to file.
   - The program will load the data and display information about the dataset.

2. **Check for Data Errors**:
   - Choose the option to check for data errors.
   - The program will identify duplicate IDs and invalid grades in the dataset and display relevant information.

3. **Generate Plots**:
   - Select the option to generate plots.
   - The program will create two plots: one showing grade distribution and another showing grades per assignment.

4. **Display List of Grades**:
   - Choose the option to display a list of grades.
   - The program will display a list of student names along with their final grades.

## Installation

Clone this repository and run `main_script.py` to access the program's functionalities.

```bash
git clone https://github.com/bertramhage/student-grades-analysis.git
cd grades-calculation
python main_script.py
