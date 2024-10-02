# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
student =["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Ian","Julia"]

def display_students():
    print(f"Current students:\n")
    for L in student:
        print(L)

# Add a new student to the list
def add_student():
    nameadd=input("what name do you want to add?")
    student.append(nameadd)
    display_students()

# Remove a student from the list by name
def remove_student():
    remove=input("what name do you want to remove?")
    if remove in student:
        student.remove(remove)
        display_students()
    else:
        print("that name is not found")
 

# remove a student from the end of the list
def pop_student():
    if len(student) == 0 : 
        print("the list is empty")
    else:
        print("the name that you remove was:")
        print(student[-1])
        student.pop()
        display_students()

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    addName = input("what name do you want to add?")
    #TODO Check if the student is in the list, then ask for the new name
    if addName in student :
        print("that name is already in the list")
    else:
        student.append(addName)
        display_students()
    #TODO Update the student's name in the list
    #TODO If the student is not found, print an error message
    #TODO display the updated list

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1" :
            add_student()
        elif choice == "2" :
            remove_student()
        elif choice == "3" :
            pop_student()
        elif choice == "4" :
            update_student()
        elif choice == "5" :
           break 
        else :
            print("wrong choice")
        #TODO depending of the user choice option (1 - 5), call the correct function

# Start the program 
menu()