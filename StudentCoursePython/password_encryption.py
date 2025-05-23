class PasswordEncryption:

    @staticmethod
    def encrypt(password):
        encrypted_password = ""
        for char in password:
            encrypted_char = chr(ord(char) + 13)

            encrypted_password += encrypted_char
        return encrypted_password


    @staticmethod
    def decrypt(password):
        decrypted_password = ""
        for char in password:
            decrypted_char = chr(ord(char) - 13)
            decrypted_password += decrypted_char
        return decrypted_password


