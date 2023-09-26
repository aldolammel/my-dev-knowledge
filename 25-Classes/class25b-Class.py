"""
CLASS IN PYTHON: TRYING A CLASS AND DICTIONARY.

A dictionary can store data. A object can store data and methods (functions that the object can execute
with access to its own data).

"""

# Using a dictionary ---------------------------------------------------------------------------------------------------
_aldoLammelDictionary = {
    'name': 'Aldo Lammel',
    'grades': [7, 8.8, 9, 9.9]
}


def fnc_averageGrade(_student):
    """
    It calcs the average grade of a student
    :param _student: a student dictionary.
    :return: the average grade of a student.
    """
    return sum(_student['grades']) / len(_student['grades'])


print(f'{_aldoLammelDictionary["name"]} average is: {fnc_averageGrade(_aldoLammelDictionary)}')


print('\n- - - -\n')  # the same, but with class -----------------------------------------------------------------------


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name  # creating the object/information.
        self.grades = new_grades  # creating another one.

    def fnc_average(self):
        return sum(self.grades) / len(self.grades)


_studentOne = Student('Aldo Lammel', [7, 8.8, 9, 9.9])

print(f'{_studentOne.name} average is: {_studentOne.fnc_average()}')
