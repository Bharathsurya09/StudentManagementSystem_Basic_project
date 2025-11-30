"""Student management system"""
import csv


#Load existing data from CSV file when program starts
def load_data():
    try:
        with open('students.csv', "r") as file:
            reader=csv.reader(file)
            for Row in reader:
                if Row not in students:
                    students.append(Row)
    except FileNotFoundError:
        pass


# save data in a CSV file
def save_data():
    unique=[]
    for Row in students:
        if Row not in unique:
            unique.append(Row)


    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for Student in students:
            if len(Student)==5:
                writer.writerows(students)
    students[:]=unique
#checking the id existence
def id_exists(student_id):
    for s in students:
        if s[0] == student_id:
            return True
    return False

# Data storage
students=[]
# Load data before showing menu
load_data()

print("=== Student management system===")
print("1.Add student\n2.View students\n3.Search student\n4.Update student\n5.Delete student\n6.Save and Exit")

#performing main operation
while True:
    choice=input("Enter your choice....:")
    if choice not in ["1","2","3","4","5","6"]:
        print("Invalid choice.please try again...")
        break


    elif choice=="1":    #Adding student details
        row=[]
        Id=input("Enter Student ID: ")
        if id_exists(Id):
            print("Student ID is already exists!...")
            continue
        Name=input("Enter Student Name: ")
        Age=input("Enter Student Age: ")
        Course=input("Enter Student Course: ")
        Marks=input("Enter Student Marks: ")
        row.append(Id)
        row.append(Name)
        row.append(Age)
        row.append(Course)
        row.append(Marks)
        students.append(row)
        print("Student Details added succesfully!..")



    elif choice=="2":      #view students details
        print("  ID\t\tName\t\tAge\t\tCourse\t\tMarks")
        for student in students:
            print(f"{student[0]}\t\t{student[1]}\t\t{student[2]}\t\t{student[3]}\t\t{student[4]} ")



    elif choice=="3":     #search student details
        search_name=input("Enter the name of the student to search: ")
        searched_user=[]
        is_found=False
        for student in students:
            if student[1]==search_name:
                searched_user.append(student)
                is_found=True
        if not is_found:
            print("Student not found")
        else:
            print("ID\t\tName\t\tAge\t\tCourse\t\tMarks")
            for student in searched_user:
                print(f"{student[0]}\t\t{student[1]}\t\t{student[2]}\t\t{student[3]}\t\t{student[4]}")



    elif choice=="4":    #update the student details
        update_det=input("Enter the column for which the details: ")
        update_id=input("Enter Student ID to update the details: ")
        is_found=False
        for student in students:
            if student[0]==update_id:
                is_found=True
                if update_det.lower()=="name":
                    new_name=input("Enter new name to update: ")
                    student[1]=new_name
                elif update_det.lower()=="age":
                    new_age=input("Enter new age to update: ")
                    student[2]=new_age
                elif update_det.lower()=="course":
                    new_course=input("Enter new course to update: ")
                    student[3]=new_course
                elif update_det.lower()=="marks":
                    new_marks=input("Enter new marks to update: ")
                    student[4]=new_marks
                else:
                    print("Invalid choice.please try again...")
                    break
                print("Student Details updated succesfully!...")
                break
        if not is_found:
            print("Student not found")



    elif choice=="5":    #Delete the student details based on
        delete_id=input("Enter Student ID to delete: ")
        is_found=False
        for student in students:
            if student[0]==delete_id:
                students.remove(student)
                is_found=True
                print("Student details deleted succesfully!...")
                break
        if not is_found:
            print("Invalid student ID.")



    elif choice=="6":     # save and exit
        save_data()
        print("Saving the data and existing...")
        break

