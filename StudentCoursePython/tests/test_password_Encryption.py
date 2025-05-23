import unittest
import password_encryption

password_encrypt = password_encryption.PasswordEncryption()
class MyTestCase(unittest.TestCase):

    def test_that_encrypt_encrypts_password(self):
        self.assertEqual("non", password_encrypt.encrypt("World"))

    def test__that_decrypt_decrypts_the_encrypted_password(self):
         self.assertEqual("aba", password_encrypt.decrypt("non"))


if __name__ == '__main__':
    unittest.main()
