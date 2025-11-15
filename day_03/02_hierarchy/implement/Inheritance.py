class Parent:
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child Method")


child = Child()
child.parent_method()