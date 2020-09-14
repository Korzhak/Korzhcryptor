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


class Lab1:
    @staticmethod
    def _get_index(text):
        """ The method of obtaining the index of the letter
        :param text: The text you want to convert to letter indexes
        :return: list of text letter indexes
        """
        return [(al.index(i.lower()) if i.lower() in al else i) for i in text]

    @staticmethod
    def caesar(key: int = 0, raw_text: str = None, encode_text: str = None):
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

    def vigenere(self, key: str = '', raw_text: str = None, encode_text: str = None):
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
            for i in range(len(raw_text_int)):
                if raw_text[i].isalpha():
                    value = (raw_text_int[i] + key_as_int[i % key_length]) % len(al)
                    encode_text += al[value]
                else:
                    encode_text += raw_text[i]

            return encode_text

        # Decoding by Vigenere
        elif encode_text and not raw_text:
            encode_text_int = self._get_index(encode_text)
            decode_text = ''
            for i in range(len(encode_text_int)):
                value = (encode_text_int[i] + key_as_int[i % key_length]) % len(al)
                decode_text += al[value]
            return decode_text

        # if got raw_text and encode_text
        raise Exception("Get me key and 'raw_text' or key and 'encode_text'")

    def polybius(self):
        pass


e = Lab1()
print(e.vigenere("olexpidor", raw_text="Bohdan Korzhak"))


