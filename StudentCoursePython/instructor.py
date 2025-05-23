import os
from user import User

class Instructor(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, "instructor")

    def create_course(self, course_name):
        if self._course_exists(course_name):
            print("Error: Course already exists.")
            return False

        with open("courses.txt", "a") as file:
            file.write(f"{course_name},{self.email}\n")
        return True

    def assign_grade(self, student_email, course_name, grade):
        if not self._course_exists(course_name):
            print("Error: Course does not exist.")
            return False

        with open("grades.txt", "a") as file:
            file.write(f"{student_email},{course_name},{grade}\n")
        return True

    @staticmethod
    def _course_exists(course_name):
        if not os.path.exists("courses.txt"):
            return False

        with open("courses.txt", "r") as file:
            return any(line.strip().startswith(course_name + ",") for line in file)
