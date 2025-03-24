from week11 import Person
class Student(Person):
    def __init__(self,p_name, p_age, p_height,  p_major):
        super().__init__(p_name, p_age, p_height)
        self.major = p_major
        print("This time it's a Student object")

student1 = Student("Maria", 22, 6, "Computer Science")
print("Student Name:", student1.name)
print("Student Major:", student1.major)
