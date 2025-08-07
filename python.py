class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def person_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
class Student(Person):
    def __init__(self, name, age, address,student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []
    def add_grade(self, subject, grade):
        if self.student_id not in self.grades:
            print('Student Id not found.')
            return