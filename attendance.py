import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


def initialize_firestore():
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
        
            

def take_attendance(db):
    pass

def display_students(db):
    pass

def modify_student(db):
    pass

def add_student(db):
    student_name = input("Student Name: ")
    result = db.collection("students").document(student_name).get()
    if result.exists:
        print("Error! \n User already exists in database!")
        return
    print("Did the student attend the following days? (y/n)")
    monday = input("Monday? >")
    tuesday = input("Tuesday? >")
    wednesday = input("Wednesday? >")
    thursday = input("Thursday? >")
    friday = input("Friday? >")

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