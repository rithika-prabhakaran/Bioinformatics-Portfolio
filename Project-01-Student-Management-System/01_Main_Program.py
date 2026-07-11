students = []
try:
        file = open("student.txt" , "r")

        for line in file:
            line = line.strip()

            if line !="":
                data = line.split(",")

                student = {"Name": data[0],
                           "Roll":data[1],
                           "Marks":int(data[2])}
                students.append(student)
        file.close()
except FileNotFoundError:
      pass
def save_students():
    file =open("student.txt" , "w")
    for student in students:
        file.write(f"{student['Name']} , {student['Roll']} , {student['Marks']}\n"
        )
        file.close()

                

while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")


    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        marks = int(input("Enter Marks: "))

        exists = False

        for student in students:
            if student["Roll"] == roll:
                exists = True
                break

        if exists:
            print("Roll Number already exists!")

        else:
            student = {
                "Name": name,
                "Roll": roll,
                "Marks": marks
            }

            students.append(student)
            
            file = open("student.txt" , "a")
            file.write(f"{name},{roll},{marks}\n")
            file.close()

            print("Student added successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            print("\nStudent Records")
            print("---------------------------")

            for student in students:
                if student ["Marks"] >= 90:
                    grade = "A"
                elif student ["Marks"] >=75:
                    grade = "B"
                elif student["Marks"]  >=50:
                    grade = "C"
                else:
                    grade = "F"
        
                print("Name :", student["Name"])
                print("Roll :", student["Roll"])
                print("Marks:", student["Marks"])
                print("Grade:", grade)
                print("---------------------------")

    # Search Student
    elif choice == "3":

        roll = input("Enter Roll Number to Search: ")

        found = False

        for student in students:
            if student["Roll"] == roll:
                print("\nStudent Found")
                print("Name :", student["Name"])
                print("Roll :", student["Roll"])
                print("Marks:", student["Marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "4":

        roll = input("Enter Roll Number to Delete: ")

        found = False

        for student in students:
            if student["Roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")


    elif choice == "5":
        roll = input("Enter Roll Number to Update: ")
        found =False
        for student in students:
            if student["Roll"] == roll:
                print("\nStudent Found")
                print("Current Name :" , student["Name"])
                print("Current Marks:" , student["Marks"])

                new_name = input("Enter New Name: ")
                new_marks = int(input("Enter New Marks: "))
                student["Name"] = new_name
                student["Marks"] = new_marks

                print("Student Updated Sucessfully!")
                found = True
                break
            if not found:
                print("Student not Found.")

    # Exit
    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")


