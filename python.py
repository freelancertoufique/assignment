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
        self.grades[subject] = grade
    def enroll_course(self,course_name):
        if self.course_name not in self.courses:
            self.courses.append(course_name)
    def display_student_info(self):
        self.person_info()
        print(f'Student id: {self.student_id}')
        print(f'Enrolled coures: {",".join(self.courses) if self.courses else "None"}')
        print(f'Grades: {self.Grades if self.grades else "None"}')
        
        