"""
CLASS IN PYTHON: INHERITANCE
When a class is the parent of other ones.

"""

# Student class is the parent:


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = list()

    def fnc_average(self):
        return sum(self.marks) / len(self.marks)


# WorkingStudent is the child class: class Name_of_your_child_class(Name_of_your_parent_class):


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


# Creating the student:
_student = WorkingStudent('Aldo', 'UNISINOS', 15.50)
print(_student.name, _student.salary)
_student.marks.append(57)
_student.marks.append(94)
print(_student.marks)
