# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

courseID = {}
add_another = True
while add_another is True:
    course_code, course_name = input("Enter a course ID and its name separated by comma: ").split(",")
    courseID[course_code] = course_name
    add_another = input("Would you like to add another course? y/n: ")
    if add_another == "y":
        add_another = True
    else:
        add_another = False

subject = input("Enter the subject code you would like to search through (ex.COS): ")

for key, value in courseID.items():
    if subject in key:
        print(f'{key}: {value}')