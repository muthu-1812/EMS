import os
import pickle

from Company import Company
from Employee import Employee

if os.path.isfile('data.pickle'):
    with open('data.pickle', 'rb') as f:
        company = pickle.load(f)
else:
    company = Company("ABC_COMPANY")


def save_data_to_pickle():
    with open('data.pickle', 'wb') as f:
        pickle.dump(company, f)


def create_department(name):
    dept = company.add_department(name)
    return dept


def remove_department(dept_name):
    company.remove_department(department_name=dept_name)

    # I can either move all employees to NO_DEPARTMENT or consider them as fired.


def create_employee(emp_id, name, pos, dept_name=None):
    if dept_name:
        dept = company.get_department(dept_name)
    else:
        dept = company.get_department("NO_DEPARTMENT")

    dept.add_employee(Employee(emp_id, name, pos))
    print(f"Created record for {name} and added to dept: {dept.name}")


def remove_employee_from_department(dept_name, emp_id):
    dept = company.get_department(dept_name)
    if dept is None:
        raise ValueError(f"Invalid dept_name {dept_name}")
    removed_emp = dept.remove_employee(emp_id)

    if removed_emp:
        dept = company.get_department("NO_DEPARTMENT")
        dept.add_employee(removed_emp)
        print(f"Employee {removed_emp.name} has been removed from {dept_name}")

    else:
        print("Employee does not belong in this department")


def display_options():
    """
    This method prints out a menu for an EMS.
    """

    options = """
    \nOptions:
    1. Add a Department to Company
    2. Remove Department
    3. Remove Employee from Department
    4. Display Departments in Company
    5. Add Employee
    6. List Employee in a Department
    7. Print Company Hierarchy
    """
    print(options)


def check_if_user_wants_to_exit():
    x = input("DO YOU WANT TO CONTINUE(y/N):")
    if x == "N":
        save_data_to_pickle()
        exit()


def main():
    # I should be using argparse
    while True:
        display_options()
        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:

            dept_name = input("Enter department name to add:")
            d = create_department(dept_name)
            print(f"Created department {d.name}")
            check_if_user_wants_to_exit()

        elif choice == 2:
            dept_name = input("Enter department name to delete:")
            remove_department(dept_name)
            print(f"{dept_name} has been removed with all of its Employees")
            check_if_user_wants_to_exit()

        elif choice == 3:
            dept_name = input("Enter department name:\n")
            emp_id = int(input("Enter id of Employee to be removed:\n"))
            remove_employee_from_department(dept_name, emp_id)
            check_if_user_wants_to_exit()

        elif choice == 4:
            print([c.name for c in company.departments])
            check_if_user_wants_to_exit()

        elif choice == 5:
            # Validate all arguments are provided
            emp_id = int(input("Enter employee id: "))
            name = input("Enter employee name: ")
            title = input("Enter employee title: ")
            department = input("Enter employee department: ")
            create_employee(emp_id, name, title, department)
            check_if_user_wants_to_exit()

        elif choice == 6:
            dept_name = input("Enter department name: ")
            dept = company.get_department(dept_name)

            if dept is None:
                raise ValueError("Enter valid department id")

            print([emp.name for emp in dept.employees])
            check_if_user_wants_to_exit()

        elif choice == 7:
            print(company)
            check_if_user_wants_to_exit()


if __name__ == '__main__':
    # TODO I have to validate if emp already created
    # TODO validate if dept already created
    # TODO Ideally I should save changes before it exits because of raising an exception

    try:
        main()
    except Exception as e:
        save_data_to_pickle()
        raise e
    # print(company.name)
    #
    # d1 = create_department("Engg")
    # print(d1.name)
    # d2 = create_department("Ops")
    # print(d2.name)
    #
    # print(company.departments)
    # create_employee(1, "muthu", "SDE", "Engg")
    # create_employee(2, "mm", "SDE")
    # create_employee(3, "gana", "SDE")
    #
    # print(company)
