# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class b"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()

c.showProps()
print(C.__mro__)
