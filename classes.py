# new class  inheritance

class Parent:
    parentAttr = 100

    def __init__(self):
        print("calling constructor")

    def parentmethod(self):
        print("calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self, ):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):

    def __init__(self):
        print("calling child constructor")

    def childMethod(self):
        print("calling child method")


c = Child()
c.childMethod()
c.parentmethod()
c.setAttr(200)
c.getAttr()


