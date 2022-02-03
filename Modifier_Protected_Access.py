class Student:

    _name = None
    _roll = None
    _branch = None

    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def _displayRollAndBranch(self):
        print("Roll:  ", self._roll)
        print("Branch:  ", self._branch)

class Geek(Student):

    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    def displayDetails(self):
        print("Name:  ", self._name)
        self._displayRollAndBranch()

obj = Geek("R2J", 1706256, "Information Technology")
obj.displayDetails()