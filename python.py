# ------------------Person Class Creation------------------
# This code defines a Person class with basic attributes and methods.

class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def person_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')

# ------------------Student Class Creation------------------
# This code defines a Student class that inherits from Person and adds student-specific attributes and methods.


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

# ------------------Course Class Creation-----------------------
# This code defines a Course class that maintain the students enrolled in course and their grades.

class Course:
    def __init__(self,course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)
    def display_course_info(self,student_dict):
        print(f'Course Name: {self.course_name}')
        print(f'Course Code: {self.course_code}')
        print(f'Instructor: {self.instructor}')
        enrolled_name = [student_dict[i].name for i in self.students if i in student_dict]
        print(f'Enrolled Students: {', '.join(enrolled_name) if enrolled_name else "None"}')

