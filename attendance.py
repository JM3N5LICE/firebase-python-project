import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


def initialize_firestore():
    """ The parameters to enable firebase and token access. """
    project_id = "attendance-eca04"

    cred = credentials.Certificate('auth.json')
    firebase_admin.initialize_app(cred, {
        'project_id': project_id,
    })

    db = firestore.client()
    return db

def main():
    db = initialize_firestore()
    choice = None
    while choice != "0":
        print()
        print("0) Exit")
        print("1) Display Students")
        print("2) Modify Individual Student Attendance")
        print("3) Add Student")
        print("4) Delete Student")

        choice = input(f"> ")
        print()

        if choice == "1":
            display_students(db)
        elif choice == "2":
            modify_student(db)
        elif choice == "3":
            add_student(db)
        elif choice == "4":
            delete_student(db)
        
        

def display_students(db):
    """ Displays all students in table. """

    results = db.collection("students").get()
    
    print("Search Results:")
    print(f"{'Student':<20} {'Monday':<10} {'Tuesday':<10} {'Wednesday':<10} {'Thursday':<10} {'Friday':<10}")
    for result in results:
        item = result.to_dict()
        print(f"{result.id:<20} {item['Monday']:<10} {item['Tuesday']:<10} {item['Wednesday']:<10} {item['Thursday']:<10} {item['Friday']:<10}")
        print()

def modify_student(db):
    """ Allows fields (days) to be modifeid. """

    student_to_modify = input("Which student would you like to modify? ")
    student = db.collection("students").document(student_to_modify).get()
    if not student.exists:
        print("Warning! \n Please enter a valid student name!")
        return
    
    info = student.to_dict()
    field = input("Which day do you want to modify? ")
    print()
    if field in info:
        new_field = input("What would you like to update the value to? ")
        print()
    else:
        print("Warning! \n Verify field exists!")
        return

    db.collection("students").document(student_to_modify).update({field : new_field})
    print(f"{student_to_modify}'s attendance on {field} changed to {new_field}")


def add_student(db):
    """ Adds a student as a document to the collection in firebase with the requisite fields. """

    student_name = input("Student Name: ")
    result = db.collection("students").document(student_name).get()
    if result.exists:
        print("Error! \n User already exists in database!")
        return
    print("Did the student attend the following days? (y/n)")
    monday = input("Monday? > ")
    tuesday = input("Tuesday? > ")
    wednesday = input("Wednesday? > ")
    thursday = input("Thursday? > ")
    friday = input("Friday? > ")

    db.collection("students").document(student_name).set({
        "Monday" : monday,
        "Tuesday" : tuesday,
        "Wednesday" : wednesday,
        "Thursday" : thursday,
        "Friday" : friday
    })
    print()
    print(f"{student_name} added to 'students'")

def delete_student(db):
    """ Searches out a specific student and removes them and their fields from the database. """
    print()
    print("Warning! \n All data that is deleted cannot be recovered!")
    print()
    deleted_student = input("Student name: ")
    result = db.collection("students").document(deleted_student).get()
    if not result.exists:
        print("Student does not exist!")
        return

    print()
    confirm = input("Are you sure you want to delete this student? (y/n) ")
    if confirm.lower() == 'y':
        db.collection("students").document(deleted_student).delete()



if __name__ == "__main__":
    main()