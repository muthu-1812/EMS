import typer
from typing_extensions import Annotated

from Employee import Employee

from pickling_utils import init_company, save_data_to_pickle

app = typer.Typer(help="Employee Management System.", rich_markup_mode="rich")

company = init_company()


def create_department(name):
    dept = company.add_department(name)
    return dept


def remove_department(dept_name):
    company.remove_department(department_name=dept_name)

    # I can either move all employees to NO_DEPARTMENT or consider them as fired.


def remove_employee_from_department(dept_name, emp_id):
    dept = company.get_department(dept_name)
    if dept is None:
        raise ValueError(f"Invalid dept_name {dept_name}")
    removed_emp = dept.remove_employee(emp_id)

    if removed_emp:
        dept = company.get_department("NO_DEPARTMENT")
        dept.add_employee(removed_emp)
        print(f"Employee {emp_id} has been removed from {dept_name}")

    else:
        print("Employee does not belong in this department")


@app.command("create_dept")
def create_department_in_company(deparment_name: Annotated[
    str, typer.Option(help="Enter name of department to be [green]created[/green]", prompt=True)
]):
    """
    Create a department by providing department name
    """
    d = create_department(deparment_name)
    print(f"Created department {d.name}")




@app.command
def remove_department(department_name: Annotated[
    str, typer.Option(help="Enter name of department to be [green]created[/green]", prompt=True)
],
                      force: Annotated[
                          bool,
                          typer.Option(
                              prompt="Are you sure you want to delete the user?",
                              help="Force deletion without confirmation.",
                          ),
                      ],
                      ):
    """
    Delete a department with DepartmentName.

    If --force is not used, will ask for confirmation.
    """
    if force:
        remove_department(department_name)
        print(f"{department_name} has been removed with all of its Employees")
    else:
        print("Deleting a department is cancelled")


@app.command("remove_emp_from_dept")
def remove_emp_from_department(dept_name: Annotated[
    str, typer.Option(help="Enter name of department from which person is [red]removed[/red]", prompt=True)
],
                               emp_id: Annotated[
                                   int, typer.Option(help="Enter id of employee to be [red]deleted[/red]",
                                                     prompt=True)
                               ],
                               force: Annotated[
                                   bool,
                                   typer.Option(
                                       prompt=True,
                                       help="Force deletion without confirmation.",
                                   ),
                               ],
                               ):
    """
    Delete a users from the mentioned department.

    If --force is not used, will ask for confirmation.
    """

    if force:
        remove_employee_from_department(dept_name, emp_id)
    else:
        print("Operation cancelled")


@app.command("display_departments")
def display_departments_in_company():
    """
    Display all departments in current company
    """
    print([c.name for c in company.departments])


@app.command("create_employee")
def create_employee(emp_id: Annotated[
    int, typer.Option(help="Enter id of employee to be [green]created[/green]", prompt=True)
], name: Annotated[str, typer.Option(help="Enter full name of the employee", prompt=True)],
                    title: Annotated[str, typer.Option(help="Enter the designation of employee", prompt=True)],
                    dept_name: Annotated[
                        str, typer.Option(help="Enter name of department to which person belongs", prompt=True)
                    ],
                    ):
    """
    Create an employee by providing emp_id,name,title,dept_name
    """
    if dept_name:
        dept = company.get_department(dept_name)
    else:
        dept = company.get_department("NO_DEPARTMENT")

    dept.add_employee(Employee(emp_id, name, title))
    print(f"Created record for {name} and added to dept: {dept.name}")


@app.command("display_emps_in_dept")
def display_all_employees_in_dept(dept_name: Annotated[
    str, typer.Option(help="Enter name of department:", prompt=True)
]):
    """

    Lists all employees working in a particular department search by dept_name
    """
    dept = company.get_department(dept_name)

    if dept is None:
        raise ValueError("Enter valid department id")

    print([emp.name for emp in dept.employees])


@app.command("company_hierarchy")
def company_hierarchy():
    """
    Displays the entire company hierarchy
    """
    print(company)


if __name__ == "__main__":

    try:
        app()
    except Exception as e:
        raise e
    finally:
        save_data_to_pickle(company)
