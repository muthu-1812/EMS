# TODO just create one instance of this
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict

from Department import Department


@dataclass
class Company:
    _name: str
    _departments: Dict[str | None, Department] = field(default_factory=dict)

    def __post_init__(self):
        self._departments["NO_DEPARTMENT"] = Department("NO_DEPARTMENT")

    @property
    def name(self):
        return self._name

    @property
    def departments(self):
        return list(self._departments.values())

    def get_department(self, dept_name):
        if dept_name:
            return self._departments[dept_name]
        else:
            return None

    def add_department(self, department_name):
        if department_name not in self._departments:
            self._departments[department_name] = Department(department_name)
            return self._departments.get(department_name)

        else:
            raise ValueError("Department already exists")

    def remove_department(self, department_name):
        if department_name in self._departments:
            del self._departments[department_name]
        else:
            raise ValueError("Department does not exist")

    def __str__(self):
        return f"{self.name}:{self.departments}"

    def __repr__(self):
        return f"{self.name}:{self.departments}"
