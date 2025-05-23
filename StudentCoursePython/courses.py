import os

class Course:
    def __init__(self, name, instructor_email):
        self.name = name
        self.instructor_email = instructor_email

    def enroll_student(self, student_email):
        if not self._course_exists():
            print("Error: Course does not exist.")
            return False

        with open("students.txt", "a") as file:
            file.write(f"{student_email},{self.name}\n")
        return True

    def _course_exists(self):
        if not os.path.exists("courses.txt"):
            return False

        with open("courses.txt", "r") as file:
            return any(line.strip().startswith(self.name + ",") for line in file)
