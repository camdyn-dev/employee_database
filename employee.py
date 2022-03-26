employee_database = []


def main():
    try:
        print("""1: Add a new employee\n2: Print all employees
3: Delete by age\n4: Update salary by name
5: Close program""")

        user_choice = int(input("Enter your choice: "))
        while user_choice < 0 or user_choice >5:
            print("Invalid input, try again")
            user_choice = int(input("Enter your choice: "))
        front_end_handler(user_choice)
    except ValueError:
        print("ERROR: Unaccepted value type! Try again...\n")
        main()


def front_end_handler(user_choice):
    if user_choice == 1:
        employee_add()  # Add an employee

    elif user_choice == 2:
        employee_print()    # Print all employees

    elif user_choice == 3:
        employee_age_delete()    # Delete employee by age range

    elif user_choice == 4:
        employee_salary_update()    # Update employee salary

    else:
        print("aite, bye bye")
        exit()


def employee_add():
    try:
        employee_name = input("Enter the employee's name: ")
        employee_age = int(input(f"Enter {employee_name}'s age: "))
        employee_salary = int(input(f"Enter {employee_name}'s salary: "))

    except ValueError:
        print("ERROR: Invalid input")



main()
