def add_grade(student_grades):
    # Prompt the user for the student's name
    student_name = input("Enter the student's name: ")
    
    # Prompt the user for the subject
    subject = input("Enter the subject: ")
    
    # Prompt the user for the grade and convert it to a float
    grade = float(input("Enter the grade: "))

    # If the student is not already in the dictionary, add them with an empty dictionary for subjects
    if student_name not in student_grades:
        student_grades[student_name] = {}
    
    # Add the grade for the subject to the student's record
    student_grades[student_name][subject] = grade
    
    # Print a confirmation message
    print(f"Added grade {grade} for {student_name} in {subject}.")

def calculate_averages(student_grades):
    # Create a dictionary to store the averages
    averages = {}
    
    # Iterate over each student and their subjects
    for student_name, subjects in student_grades.items():
        # Calculate the total of all grades for the student
        total = sum(subjects.values())
        
        # Calculate the average grade for the student
        average = total / len(subjects)
        
        # Store the average in the averages dictionary
        averages[student_name] = average
    
    # Return the averages dictionary
    return averages

def display_student_grades_and_average(student_grades, student_name):
    # Check if the student exists in the records
    if student_name not in student_grades:
        print(f"No grades found for {student_name}.")
        return

    # Get the subjects and grades for the student
    subjects = student_grades[student_name]
    
    # Calculate the average grade for the student
    average = sum(subjects.values()) / len(subjects)
    
    # Print the grades for each subject
    print(f"\nGrades for {student_name}:")
    for subject, grade in subjects.items():
        print(f"  {subject}: {grade}")
    
    # Print the average grade
    print(f"  Average: {average:.2f}")

def main():
    # Create a dictionary to store student grades
    student_grades = {}
    
    while True:
        # Print the options for the user
        print("\nOptions:")
        print("1. Add grade")
        print("2. Search for student's grades and average")
        print("3. Quit")

        # Get the user's choice
        choice = input("Enter your choice: ")
        
        # Add a grade
        if choice == '1':
            add_grade(student_grades)
        
        # Search for a student's grades and average
        elif choice == '2':
            # Check if there are any students
            if not student_grades:
                print("No students are available.")
            else:
                # Prompt the user for the student's name
                student_name = input("Enter the student's name to search: ")
                display_student_grades_and_average(student_grades, student_name)
        
        # Quit the program
        elif choice == '3':
            break
        
        # Handle invalid choices
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
