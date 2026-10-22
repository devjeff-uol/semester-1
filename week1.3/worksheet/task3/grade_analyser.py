# Worksheet 1.3: Task 3
import sys
# Your code for the overall grade classification

# ask for filename of the student file
filename = input("Enter the name of the student data file: ").split(".csv")[0]  # remove the .csv extension if provided

student_data = []
student_grades = []

# open the file
try:
    with open(filename + ".csv", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:  # skip the header line
            # read each line, strip whitespace and split by comma
            student_data.append(line.strip().split(","))
except:
    sys.exit(f"Error: Could not open file {filename}.csv. Please check the file name and try again.")

# read in the data, and for each student calculate their average grade and classification
for student in student_data:
    student_id = student[0]
    grades = [int(grade) for grade in student[1:] if grade]
    average_grade = sum(grades) / len(grades)
    if average_grade >= 70:
        classification = "1"
    elif average_grade >= 60:
        classification = "2:1"
    elif average_grade >= 50:
        classification = "2:2"
    elif average_grade >= 40:
        classification = "3"
    else:
        classification = "F"
    
    student_grades.append((student_id, average_grade, classification))

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'
with open(filename + "_out.csv", "w") as outfile:
    for student_id, average_grade, classification in student_grades:
        outfile.write(f"{student_id},{average_grade:.2f},{classification}\n")

# You can compare your output files with the 4 example files in example_outfiles folder