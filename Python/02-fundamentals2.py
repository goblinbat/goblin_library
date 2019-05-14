"""
Try/except blocks, global variables, loops, classes
"""

# CRUD functionality: Create/add, Read/ view, Update, Delete


def palindrome(word):       # def name(parameters)
    if word == word[::-1]:
        return True
    else:
        return False

x = input('enter a word: ')
print(palindrome(x))        # arguments are what you put in the ()


# TRY/ EXCEPT
try:
    a = int(input('enter a number: '))
except Exception:
    print("can't add a string, try a number")
    exit()


# GLOBAL VARIABLES
global_var = 10

def print_global():
    # global global_var
    global_var = 11
    print(global_var)

print_global()
print(global_var)


# LOOPS
# for everything in some collection/range, do this
# while something is true, keep looping (can potentially be infinite; be careful)
x = int(input('Enter a number between 1 and 20: '))
while True:
    if x <= 10:
        print('fish')
        x += 1
    elif 10 < x < 20:
        print('bird')
        x += 1
    elif x >= 20:
        print('cheese')
        break

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in days_of_the_week:
    if day is 'Saturday' or day is 'Sunday':
        print("it's the weekend")
        print(day)
    else:
        print(day)


# CLASSES
class Student:       # class name is capitalized
    sample_name = "Dot"
    def __init__(self, name, student_id):
        self.student_name = name
        self.student_id = student_id
    def change_name(self, name):
        self.student_name = name
student = Student('fred', 1)  # creates instance of class
print(student.sample_name)    # says go into the 'sample' class and grab the string
print(student.student_name)   # retrieves the instance's student_name quality
student.change_name('carol')  # calls change_name function from inside class
print(student.student_name)
