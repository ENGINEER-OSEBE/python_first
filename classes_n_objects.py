on_honour_role = True
class Student:
    def __init__(self,name,age,height,gpa):
        self.name = name
        self.age = age
        self.height = height
        self.gpa = gpa

    def on_honour_role(self):
        if self.gpa>= 3.5:
            return True
        else:
            return False


