import os
from user import User

class Student(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, "student")

    def enroll_course(self, course_name):
        if not self._course_exists(course_name):
            print("Error: Course does not exist.")
            return False

        with open("students.txt", "a") as file:
            file.write(f"{self.email},{course_name}\n")
        return True

    @staticmethod
    def view_grades(email):
        if not os.path.exists("grades.txt"):
            print("No grades available.")
            return

        with open("grades.txt", "r") as file:
            for line in file:
                student_email, course_name, grade = line.strip().split(',')
                if student_email == email:
                    print(f"Course: {course_name}, Grade: {grade}")

    @staticmethod
    def _course_exists(course_name):
        if not os.path.exists("courses.txt"):
            return False

        with open("courses.txt", "r") as file:
            return any(line.strip().startswith(course_name + ",") for line in file)
