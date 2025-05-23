from user import User
from students import Student
from instructor import Instructor

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            role = input("Enter role (student/instructor): ").lower()

            if email in User.map_email():
                print("Error: Email already exists!")
            else:
                user = Student(name, email, password) if role == "student" \
                    else Instructor(name, email, password)
                if user.save_user():
                    print(f"{role.capitalize()} registered successfully!")

        elif choice == "2":
            email = input("Enter email: ")
            password = input("Enter password: ")

            if User.login(email, password):
                user_data = User.map_email().get(email)
                print(f"Welcome, {user_data['name']}!")

                if user_data["role"] == "instructor":
                    instructor = Instructor(user_data["name"], email, password)
                    while True:
                        print("\n1. Create Course\n2. Assign Grade\n3. Logout")
                        action = input("Choose an option: ")
                        if action == "1":
                            course_name = input("Enter course name: ")
                            instructor.create_course(course_name)
                        elif action == "2":
                            course_name = input("Enter course name: ")
                            student_email = input("Enter student email: ")
                            grade = input("Enter grade: ")
                            instructor.assign_grade(student_email, course_name, grade)
                        elif action == "3":
                            break

                else:
                    student = Student(user_data["name"], email, password)
                    while True:
                        print("\n1. Enroll in Course\n2. View Grades\n3. Logout")
                        action = input("Choose an option: ")
                        if action == "1":
                            course_name = input("Enter course name: ")
                            student.enroll_course(course_name)
                        elif action == "2":
                            student.view_grades(email)
                        elif action == "3":
                            break

            else:
                print("Invalid details.")

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
