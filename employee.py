# Might update this to use SQL so it's more like a real-world app, but this is just a fun project so I probably won't

# Would've used a class, but I don't remember how OOP works in python so functions are good
def space():
    print("")   # Pretty much \n but ez-er to put throughout the program


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
        print("-- Main Menu --")
        print("""
1: Add a new employee
2: Print all employees
3: Delete by age
4: Update salary by name
5: Close program
""")

        user_choice = int(input("Enter your choice: "))
        while user_choice < 0 or user_choice > 5:
            print("That input is not within range.\nTry again...")
            user_choice = int(input("Enter your choice: "))
        front_end_handler(user_choice)
    except ValueError:
        print("ERROR: Unaccepted value type!\nTry again...")
        main()


def front_end_handler(user_choice):
    space()
    if user_choice == 1:
        employee_add()  # Add an employee

    elif user_choice == 2:
        employee_print()    # Print all employees

    elif user_choice == 3:
        employee_ageism()    # Delete employee by age range

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

        space()
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

        space()
        main()

    else:
        print("lmao ur workforce is 2021 style: G O N E")
        main()


def employee_ageism():
    try:
        print("-- Ageism --")
        global employee_database    # Using this so I can reassign it to the new list
        # Now, the only problem is that it can possibly be slower for new lists, but I don't imagine it'll
        # be much slower. Honestly, could actually be faster since I don't have to use .pop or other methods

        post_ageism = []

        lower_range = int(input("Enter the lower end of ages: "))
        upper_range = int(input("Enter the upper end of ages: "))

        for employee in employee_database:
            if employee["age"] < lower_range or employee["age"] > upper_range:
                post_ageism.append(employee)    # append instead of push? M A D G E

            else:
                print(f"{employee['name']} has been removed.")
        employee_database = post_ageism

        space()
        main()

    except ValueError:
        print("ERROR: Invalid input")
        print("Try again...")

        employee_ageism()


def employee_salary_update():
    try:
        print("-- Salary Updater --")
        found = False
        employee_name = input("Enter the employee's name: ")
        employee_salary = int(input(f"Enter {employee_name}'s new salary: "))

        for employee in employee_database:
            if employee_name == employee["name"]:
                employee["salary"] = employee_salary
                found = True

        if found:
            print(f"{employee_name}'s salary was successfully updated.")

            space()
            main()

        else:
            print("We couldn't find that employee. Try again.")
            employee_salary_update()

    except ValueError:
        print("ERROR: Invalid input")
        print("Try again...")

        employee_salary_update()


main()
