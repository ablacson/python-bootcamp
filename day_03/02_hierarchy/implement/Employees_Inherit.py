class Employee:
    def __init__(self, name, id, tasks): # What does this do
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {name} with ID {id}, a task of {tasks} created.")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

employee1 = Employee("Richard", "1234", "Working")
employee2 = Employee("Somnus", "777", "Working")

class Recruiter(Employee):
    def recruit(self):
        self.add_work("recruit")
recruiter1 = Recruiter("Recruiter1", 7777, "Recruiting")
recruiter2 = Recruiter("Recruiter", 1234, "Recruiting")

class Developer(Employee):
    def code(self):
        self.add_work("code")
developer1 = Developer("Developer1", 1234, "Developing")
developer2 = Developer("Developer2", 1234, "Developing")


class Manager(Employee):
    def manage(self):
        self.add_work("manage")

manager1 = Manager("Manager1", 1234, "Managing")
manager2 = Manager("Manager2", 2323, "Managing")