import json

def write_to_json(student_details):
    with open('StudentJson.json', 'w') as file:
        json.dump(student_details, file)

def read_from_json():
    with open('StudentJson.json', 'r') as file:
        student_details = json.load(file)
    return student_details

# Get user input for student details
name = input("Enter student name: ")
student_id = int(input("Enter student ID: "))
course = input("Enter student course: ")

# Create initial student details dictionary
student_details = {
    "Name": name,
    "ID": student_id,
    "Course": course
}

# Write the initial details to the JSON file
write_to_json(student_details)

# Read the details from the JSON file
loaded_student_details = read_from_json()

# Display the initial details
print("Details of the Student are")
for key, value in loaded_student_details.items():
    print(f"\t{key}: {value}")

# Append additional CourseDetails
course_group = input("Enter course group: ")
course_year = int(input("Enter course year (Only Numbers): "))

loaded_student_details["CourseDetails"] = {
    "Group": course_group,
    "Year": course_year
}

# Write the updated details to the JSON file
write_to_json(loaded_student_details)

# Display the updated details
print("Details of the Student are")
for key, value in loaded_student_details.items():
    print(f"\t{key}: {value}")
