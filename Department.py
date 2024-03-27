from dataclasses import dataclass, field
from typing import List

from Employee import Employee


@dataclass
class Department:
    _name: str
    _employees: List[Employee] = field(default_factory=list)

    @property
    def name(self):
        return self._name

    @property
    def employees(self):
        return self._employees

    def add_employee(self, employee: Employee):

        # TODO I have to remove from previous department
        # TODO Update employee propery as well
        # TODO add it to current department

        self._employees.append(employee)

    def remove_employee(self, employee_id):

        for employee in self._employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                return Employee

        return None



    def list_employees(self):
        """
        The list_employees method prints the employees in a specific department.
        """

        # TODO use a generator here
        for employee in self.employees:
            print(employee.display_details())

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Department):
            return False
        return self.name == other.name

    def __str__(self):
        return f"{self.name}:{self.employees}"

    def __repr__(self):
        return f"{self.name}:{self.employees}"
