"""
CLASS INHERENT: SUPER()

    It's a function used to give access to the methods of a parent class.
    It returns a temporary object of a parent class when used.

"""


class Person:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name


class Professor(Person):
    def __init__(self, f_name, l_name, t_status, h_date, f_date):
        super().__init__(f_name, l_name)
        self.t_status = t_status
        self.h_date = h_date
        self.f_date = f_date

    def show_profile(self):
        return (
            f"Name: {self.f_name} {self.l_name}\n"
            f"Teaching Status: {self.t_status}\n"
            f"Hired date: {self.h_date}\n"
            f"Fired date: {self.f_date}\n"
        )


class Student(Person):
    def __init__(self, f_name, l_name, l_status, dt_enroll, dt_closure):
        super().__init__(f_name, l_name)
        self.l_status = l_status
        self.dt_enroll = dt_enroll
        self.dt_closure = dt_closure

    def show_profile(self):
        return (
            f"Name: {self.f_name} {self.l_name}\n"
            f"Learning Status: {self.l_status}\n"
            f"Enroll date: {self.dt_enroll}\n"
            f"Closure date: {self.dt_closure}\n"
        )


professor1 = Professor("Pitagoras", "Junior", "Arrested", "2000 a.C.", None)
print(professor1.show_profile())

student1 = Student("Aldo", "Lammel", "Studying", "01/03/2022", None)
print(student1.show_profile())
