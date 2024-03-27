from dataclasses import dataclass


@dataclass
class Employee:
    _id: int
    _name: str
    _title: str
    # _department: str | None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    # @property
    # def department(self):
    #     return self._department

    @title.setter
    def title(self, new_title):
        self._title = new_title

    # @department.setter
    # def department(self, new_department):
    #     self._department = new_department

    def display(self):
        return f"[ID:{self.id}, Name: {self.name}, Title: {self.title}]"

    def __str__(self):
        return f"[ID:{self.id}, Name: {self.name}]"

    def __repr__(self):
        return f"[ID:{self.id}, Name: {self.name}]"


if __name__ == '__main__':
    e1 = Employee(1, "muthu", "SDE", "Engg")
    print(e1)