# I don't even remotely remember how OOP works in Python, so I'm just going to write helper functions instead
# Probably gonna write a space function which just writes new lines


employee_database = [
    {"name": "Jeff",
     "age": 10,
     "salary": 0},
    {"name": "Joe",
     "age": 25,
     "salary": 25000}
]


def main():
    try:
        print("""1: Add a new employee\n2: Print all employees
3: Delete by age\n4: Update salary by name
5: Close program""")

        user_choice = int(input("Enter your choice: "))
        while user_choice < 0 or user_choice > 5:
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
        print("-- Enter employee information --")
        employee_name = input("Enter the employee's name: ")
        employee_age = int(input(f"Enter {employee_name}'s age: "))
        employee_salary = int(input(f"Enter {employee_name}'s salary: "))

        employee_database.append({"name": employee_name, "age": employee_age, "salary": employee_salary})
        print(f"{employee_name} has been successfully added to the database.")

        main()

    except ValueError:
        print("ERROR: Invalid input")
        print("Try again...")

        employee_add()


def employee_print():
    if employee_database:
        print("-- Employee list --")
        for employee in employee_database:
            print(f"{employee['name']}: {employee['age']} years old, makes ${employee['salary']} yearly.")
        main()

    else:
        print("lmao ur workforce is 2021 style: G O N E")
        main()


def employee_age_delete():
    print("-- Ageism --")
    global employee_database    # Using this so I can reassign it to the new list
    post_ageism = []

    lower_range = int(input("Enter the lower end of ages: "))
    upper_range = int(input("Enter the upper end of ages: "))

    for employee in employee_database:
        if employee["age"] < lower_range or employee["age"] > upper_range:
            post_ageism.append(employee)    # append instead of push? M A D G E
        else:
            print(f"{employee['name']} removed")
    employee_database = post_ageism

    main()


main()
