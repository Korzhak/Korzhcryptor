"""
Name: Lab #4
Author: Bohdan Korzhak
Group: AKSm-19-1
Description: Encryptor by Cipher of Gronsfeld
"""
from string import (
    ascii_lowercase as al,
)


class NumberCipher:
    def __init__(self, date_key: str = "", number_key: int = 0):
        """Date Shift Cipher or Gronsfeld Cipher
        For use Date Shift Cipher give me *date_key*
        For use Gronsfeld Cipher give me *number_key*
        :param date_key: date of your birthday. Example: 17/02/1998
        :param number_key: number key. Example: 1234
        """
        if date_key and not number_key:
            self.key = self._parse_date(date_key)
            self.key_length = len(self.key)
            self.key_separated = [i for i in self.key]
        elif number_key and not date_key:
            self.key = str(number_key)
            self.key_length = len(self.key)
            self.key_separated = [i for i in self.key]
        else:
            raise Exception("Only one argument was expected")

    @staticmethod
    def _parse_date(date_key):
        if len(date := date_key.split("/")) == 3:
            return ''.join(date)
        raise Exception("Numbers must be separated by a \"/\" character\nFor example 23/04/2020")

    @staticmethod
    def _get_index(text: str) -> list:
        """ The method of obtaining the index of the letter
        :param text: The text you want to convert to letter indexes
        :return: list of text letter indexes
        """
        return [(al.index(i.lower()) if i.lower() in al else i) for i in text]

    def encode(self, raw_text: str = None) -> str:
        """ Encoding text by Date Shift Cipher
        :param raw_text: text for encode
        :return: encoded text
        """
        raw_text_int = self._get_index(raw_text)
        encode_text = ''
        i = 0
        max_i = len(raw_text_int)
        while i < max_i:
            while not type(raw_text_int[i]) == int:
                encode_text += raw_text_int.pop(i)
                max_i -= 1
            value = (raw_text_int[i] + int(self.key_separated[i % self.key_length])) % len(al)
            encode_text += al[value]
            i += 1

        return encode_text

    def decode(self, encode_text: str = None) -> str:
        """ Decoding text by Date Shift Cipher
        :param encode_text: text for decode
        :return: decoded text
        """
        encode_text_int = self._get_index(encode_text)
        decode_text = ''
        i = 0
        max_i = len(encode_text_int)
        while i < max_i:
            while not type(encode_text_int[i]) == int:
                decode_text += encode_text_int.pop(i)
                max_i -= 1
            value = (encode_text_int[i] - int(self.key_separated[i % self.key_length])) % len(al)
            decode_text += al[value]
            i += 1

        return decode_text


df = NumberCipher(number_key=1234)
print(df.encode("Korzhak Bohdan"))
print(df.decode("lqudicn fpjgeo"))
