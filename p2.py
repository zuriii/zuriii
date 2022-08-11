# classes

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total employee%d" % Employee.empCount)

    def displayemployee(self):
        print("employee name: ", self.name, "salary : ", self.salary)


# object

emp1 = Employee("zuri", 2000)
emp2 = Employee("zara", 5000)

emp1.displayemployee()
emp2.displayemployee()
print("total employees: %d" % Employee.empCount)
print("Employee.__doc__: ", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


# new class

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt2

print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3












