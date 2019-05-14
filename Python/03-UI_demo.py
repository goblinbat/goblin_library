"""
Simpler than the ones in the UI_examples folder

we want a menu:
Add students to list    x
List all students       x
Clear the list          x
Exit                    x
"""

import os

students = []


def prompt():
    print("Student Manager:\n" +
          "1) Add student\n" +
          "2) List student\n" +
          "3) Clear List\n" +
          "4) Exit\n")


def choice(option):
    if option == "1":
        tmp = input("Student's name: ")
        students.append(tmp)
    elif option == "2":
        if students:
            for student in students:
                print(student)
        else:
            print("no students")
    elif option == "3":
        students.clear()
        print("cleared")
    elif option == "4":
        exit(1)
    else:
        print("invalid selection")


while True:
    os.system('cls||clear')
    prompt()
    option = input("\n> ")
    choice(option)
    input("*Continue*")

