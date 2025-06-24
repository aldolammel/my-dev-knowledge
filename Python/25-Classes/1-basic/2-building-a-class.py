"""
CLASS IN PYTHON: TRYING A CLASS AND DICTIONARY.

A dictionary can store data. A object can store data and methods (functions that the object can execute
with access to its own data).

"""

# Using a dictionary ---------------------------------------------------------------------------------------------------
dict_ = {
    'name': 'Aldo Lammel',
    'grades': [7, 8.8, 9, 9.9]
}


def average_grade(student):
    """
    It calcs the average grade of a student
    :param student: a student dictionary.
    :return: the average grade of a student.
    """
    return sum(student['grades']) / len(student['grades'])


print(f'{dict_["name"]} average is: {average_grade(dict_)}')


print('\n- - - -\n')  # the same, but with class -----------------------------------------------------------------------


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name  # creating the object/information.
        self.grades = new_grades  # creating another one.

    def average(self):
        return sum(self.grades) / len(self.grades)


student_1 = Student('Aldo Lammel', [7, 8.8, 9, 9.9])

print(f'{student_1.name} average is: {student_1.average()}')
