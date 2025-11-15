
class Employee:
    def __init__(self, name, id): # What does this do
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {name} with id {id} created.")


    def work(self, task):
            print(f"{self.name} working {task}...")
            self.tasks.append(task)

employee1 = Employee("Richard", "1234")
employee2 = Employee("Somnus", "7777")

employee1.work("Creates Slides")
employee2.work("Do research")