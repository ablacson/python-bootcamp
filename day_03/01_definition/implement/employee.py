
class Employee:
    def __init__(self, name, id): # What does this do
        self.name = name
        self.id = id
        print(f"Employee {name} with {id} created.")

employee1 = Employee("Richard", "1234")
# employee1.name = "Richard"
# employee1.id = "1234"
# # print(employee1.name, employee1.id)

employee2 = Employee("Somnus", "777")
# employee2.name = "This one overwrites it?"
# employee2.id = "7777"
# print(employee2.name)
# print(employee2.name, employee2.id)