"""
Name: Lab #6
Author: Bohdan Korzhak
Group: AKSm-19-1
Description: Encryptor by Cipher of Playfair
"""

class PlayfairCipher:
    def __init__(self, key_value: str = ""):
        self.key = key_value
        self.key_matrix = self._matrix(self.key)

    @staticmethod
    def _matrix(key_value):
        matrix = []
        for e in key_value.upper():
            if e not in matrix:
                matrix.append(e)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for e in alphabet:
            if e not in matrix:
                matrix.append(e)

        # initialize a new list. Is there any elegant way to do that?
        matrix_group = []
        for e in range(5):
            matrix_group.append('')

        # Break it into 5*5
        matrix_group[0] = matrix[0:5]
        matrix_group[1] = matrix[5:10]
        matrix_group[2] = matrix[10:15]
        matrix_group[3] = matrix[15:20]
        matrix_group[4] = matrix[20:25]
        return matrix_group

    @staticmethod
    def message_to_digraphs(message_original):
        # Change it to Array. Because I want used insert() method
        message = []
        for e in message_original:
            message.append(e)

        # Delet space
        for unused in range(len(message)):
            if " " in message:
                message.remove(" ")

        # If both letters are the same, add an "X" after the first letter.
        i = 0
        for e in range(round(len(message) / 2)):
            if message[i] == message[i + 1]:
                message.insert(i + 1, 'X')
            i = i + 2

        # If it is odd digit, add an "X" at the end
        if len(message) % 2 == 1:
            message.append("X")
        # Grouping
        i = 0
        new = []
        for x in range(1, round(len(message) / 2 + 1)):
            new.append(message[i:i + 2])
            i = i + 2
        return new

    def find_position(self, letter: str):
        x = y = 0
        for i in range(5):
            for j in range(5):
                if self.key_matrix[i][j] == letter.upper():
                    x = i
                    y = j
        return x, y

    @staticmethod
    def cipher_to_digraphs(cipher):
        i = 0
        new = []
        for x in range(round(len(cipher) / 2)):
            new.append(cipher[i:i + 2])
            i = i + 2
        return new

    def encode(self, raw_text):
        raw_text = self.message_to_digraphs(raw_text)
        cipher = []
        for e in raw_text:
            p1, q1 = self.find_position(e[0])
            p2, q2 = self.find_position(e[1])
            if p1 == p2:
                if q1 == 4:
                    q1 = -1
                if q2 == 4:
                    q2 = -1
                cipher.append(self.key_matrix[p1][q1 + 1])
                cipher.append(self.key_matrix[p1][q2 + 1])
            elif q1 == q2:
                if p1 == 4:
                    p1 = -1
                if p2 == 4:
                    p2 = -1
                cipher.append(self.key_matrix[p1 + 1][q1])
                cipher.append(self.key_matrix[p2 + 1][q2])
            else:
                cipher.append(self.key_matrix[p1][q2])
                cipher.append(self.key_matrix[p2][q1])
        return cipher

    def decode(self, encoded_text):
        encoded_text = self.cipher_to_digraphs(encoded_text)
        plaintext = []
        for e in encoded_text:
            p1, q1 = self.find_position(e[0])
            p2, q2 = self.find_position(e[1])
            if p1 == p2:
                if q1 == 4:
                    q1 = -1
                if q2 == 4:
                    q2 = -1
                plaintext.append(self.key_matrix[p1][q1 - 1])
                plaintext.append(self.key_matrix[p1][q2 - 1])
            elif q1 == q2:
                if p1 == 4:
                    p1 = -1
                if p2 == 4:
                    p2 = -1
                plaintext.append(self.key_matrix[p1 - 1][q1])
                plaintext.append(self.key_matrix[p2 - 1][q2])
            else:
                plaintext.append(self.key_matrix[p1][q2])
                plaintext.append(self.key_matrix[p2][q1])

        for unused in range(len(plaintext)):
            if "X" in plaintext:
                plaintext.remove("X")

        output = ""
        for e in plaintext:
            output += e
        return output.lower()


key = "thisismykey"
message = "bohdan Korzhak is student"

p = PlayfairCipher(key_value=key)

for i in p.key_matrix:
    print(i)

encoded_message = "".join(p.encode(message))

print(encoded_message)

print("".join(p.decode(encoded_message)))

