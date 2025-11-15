class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduction(self):
        return f'Hello, I am {self.first_name} {self.last_name}.'


class Student(Person):
    def introduction(self):
        return super().introduction() + " I am not quite alive."

student = Student ("Somnus", "Caelum")
print(student.introduction())