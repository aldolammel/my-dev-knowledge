

class Person:
    def __init__(self):
        self.personal_id = int
        self.nationality = list()
        self.first_name = ""
        self.last_name = ""
        self.birthdate = ""
        self.genre = list()
        self.address = Address()
        self.phone = ""

    def update(self):
        pass


class Professor(Person):
    def __init__(self):
        super().__init__()
        self.university_id = int
        self.teaching_period = ["Morning", "Noon", "Evening"]
        self.subject = ["Mathematics", "Languages", "Sciences"]
        self.work_status = ""
        self.hired_date = ""
        self.fired_date = None


class Student(Person):
    def __init__(self):
        super().__init__()
        self.university_id = int
        self.learning_period = []
        self.learning_status = ""
        self.enroll_date = ""
        self.closure_date = None


class Address:
    def __init__(self):
        self.street = ""
        self.neighborhood = ""
        self.city = ""
        self.state = list()

    def change_address(self):
        pass
