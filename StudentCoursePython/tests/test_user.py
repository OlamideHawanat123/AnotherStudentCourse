import unittest
import user
import students

class MyTestCase(unittest.TestCase):
    def test_that_student_can_login_with_correct_details(self):
        stud = students.Student("Olamide", "raheemolamide@gmail.com", "password")
        stud.login("raheemolamide@gmail.com", "password")
        self.assertEqual()




if __name__ == '__main__':
    unittest.main()
