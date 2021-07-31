class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass_fail(self):
        if self.marks >= 40:
            print(self.name, "has", self.marks, "marks")
            return True
        else:
            print(self.name, "has", self.marks, "marks")
            return False

student1_data = Student("Student 1", 50)
student1_result = student1_data.check_pass_fail()

student2_data = Student("Student 2", 30)
student2_result = student2_data.check_pass_fail()