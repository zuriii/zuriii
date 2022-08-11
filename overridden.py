class Parent():
    def myMethod(self):
        print("calling parent")


class Child(Parent):
    def myMethod(self):
        print("calling child")


c = Child()
c.myMethod()


class Parent():

    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)


class Child(Parent):

    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()