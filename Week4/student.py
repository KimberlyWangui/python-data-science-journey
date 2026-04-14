class Student:
    def __init__(self, name, studentID, major, year_of_study):
        self.name = name
        self.studentID = studentID
        self.major = major
        self.year_of_study = year_of_study
        self.courses = {} # Key is course name, value is grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.studentID}")
        print(f"Major: {self.major}")
        print(f"Year of Study: {self.year_of_study}")
        if self.courses:
            print("Courses and Grades:")
            for course, grade in self.courses.items():
                print(f"  {course}: {grade}")
        else:
            print("No courses enrolled yet.")

    def add_course(self, course_name, grade):
        self.courses[course_name] = grade

    def remove_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]
        else:
            print(f"Course {course_name} not found in enrolled courses.")

    def calculate_gpa(self):
        if not self.courses:
            return 0
        
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        return gpa
    
    def academic_standing(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.0:
            return "Good Standing"
        else:
            return "Probation"
        
Masha = Student("Masha", "12345", "Computer Science", 2)
Masha.add_course("Data Structures", 3.5)
Masha.add_course("Algorithms", 3.0)
Masha.add_course("Operating Systems", 2.5)
Masha.add_course("Databases", 3.0)
Masha.display_info()
print(f"GPA: {Masha.calculate_gpa()}")
print(f"Academic Standing: {Masha.academic_standing()}")

Bob = Student("Bob", "67890", "Mathematics", 3)
Bob.add_course("Calculus", 2.5)
Bob.add_course("Linear Algebra", 2.0)
Bob.add_course("Abstract Algebra", 2.5)
Bob.add_course("Statistics", 3.0)
Bob.remove_course("Linear Algebra")
Bob.display_info()
print(f"GPA: {Bob.calculate_gpa()}")
print(f"Academic Standing: {Bob.academic_standing()}")