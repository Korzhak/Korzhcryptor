"""
Name: Lab #1
Author: Bohdan Korzhak
Group: AKSm-19-1
Description: Encryptor by Caesar Cipher, Vigenere Cipher
             or Polybius square
"""


from string import (
    ascii_lowercase as al,
    ascii_uppercase as au,
    ascii_letters as a_let
)


class SimpleEncryption:
    @staticmethod
    def _get_index(text: str) -> list:
        """ The method of obtaining the index of the letter
        :param text: The text you want to convert to letter indexes
        :return: list of text letter indexes
        """
        return [(al.index(i.lower()) if i.lower() in al else i) for i in text]

    @staticmethod
    def caesar(key: int = 0, raw_text: str = None, encode_text: str = None) -> str:
        """ Encoding and decoding text by Caesar Cipher
        :param key: shift key
        :param raw_text: text for encoding (if exists)
        :param encode_text: text for decoding (if exists)
        :return: encoded or decoded text
        """
        # Encoding by Caesar
        if raw_text and not encode_text:
            encoded = ''
            for letter in raw_text:
                if letter in al:
                    encoded += al[(al.index(letter) + key) % len(al)]
                elif letter in au:
                    encoded += au[(au.index(letter) + key) % len(au)]
                else:
                    encoded += letter
            return encoded

        # Decoding by Caesar
        elif encode_text and not raw_text:
            decoded = ''
            for letter in encode_text:
                if letter in al:
                    decoded += al[(al.index(letter) - key) % len(al)]
                elif letter in au:
                    decoded += au[(au.index(letter) - key) % len(au)]
                else:
                    decoded += letter
            return decoded

        # if got raw_text and encode_text
        raise Exception("Get me key and 'raw_text' or key and 'encode_text'")

    def vigenere(self, key: str = '', raw_text: str = None, encode_text: str = None) -> str:
        """ Encoding and decoding text by Vigenere Cipher
        :param key: shift key
        :param raw_text: text for encoding (if exists)
        :param encode_text: text for decoding (if exists)
        :return: encoded or decoded text
        """
        key_length = len(key)
        key_as_int = self._get_index(key)

        # Encoding by Vigenere
        if raw_text and not encode_text:
            raw_text_int = self._get_index(raw_text)
            encode_text = ''
            i = 0
            for i in range(len(raw_text_int)):
                if raw_text[i].isalpha():
                    value = (raw_text_int[i] + key_as_int[i % key_length]) % len(al)
                    encode_text += al[value]
                else:
                    # add raw symbol to text
                    encode_text += raw_text[i]

            return encode_text

        # Decoding by Vigenere
        elif encode_text and not raw_text:
            encode_text_int = self._get_index(encode_text)
            decode_text = ''
            for i in range(len(encode_text_int)):
                if encode_text[i].isalpha():
                    value = (encode_text_int[i] - key_as_int[i % key_length]) % len(al)
                    decode_text += al[value]
                else:
                    # add raw symbol to text
                    decode_text += encode_text[i]

            return decode_text

        # if got raw_text and encode_text
        raise Exception("Get me key and 'raw_text' or key and 'encode_text'")


class Polybius:
    def __init__(self):
        self.matrix = [['a', 'b', 'c', 'd', 'e'],
                       ['f', 'g', 'h', 'i', 'k'],
                       ['l', 'm', 'n', 'o', 'p'],
                       ['q', 'r', 's', 't', 'u'],
                       ['v', 'w', 'x', 'y', 'z']]

    def _get_indexes(self, symbol):
        """ The method of obtaining the index of the letter
        :param text: The letter you want to convert to letter indexes
        :return: list of the letter indexes
        """
        for x in range(len(self.matrix)):
            if symbol in (row := ''.join(self.matrix[x])):
                return [x, row.index(symbol)]

    def encode(self, raw_text):
        """ The method of encoding raw text
        :param raw_text:  text for encoding
        :return: encoded text
        """
        encode_text = ''
        for i in raw_text.lower().replace('j', 'i'):
            c = self._get_indexes(i)
            encode_text += self.matrix[(c[0] + 1) % 5][c[1]]


        return encode_text

    def decode(self, encode_text):
        """ The method of decoding for encoded text
        :param encode_text: text for decodign
        :return: decoded text
        """
        decode_text = ''
        for i in encode_text.lower().replace('j', 'i'):
            c = self._get_indexes(i)
            decode_text += self.matrix[(c[0] - 1) % 5][c[1]]

        return decode_text


se = SimpleEncryption()
c_e = se.caesar(3, "Bohdan Korzhak")
c_d = se.caesar(3, encode_text=c_e)
print(f"\tШифр Цезаря\nКлюч 3, зашифрований текст: \"{c_e}\", розшифрований \"{c_d}\"")

v_e = se.vigenere("cipher", "Bohdan Korzhak")
v_d = se.vigenere("cipher", encode_text=v_e)
print(f"\tШифр Віженера\nКлюч \"cipher\", зашифрований текст: \"{v_e}\", розшифрований \"{v_d}\"")

p = Polybius()
p_e = p.encode("BohdanKorzhak")
p_d = p.decode(encode_text=p_e)
print(f"\tШифр Полібія\nЗашифрований текст: \"{p_d}\", розшифрований \"{p_e}\"")
