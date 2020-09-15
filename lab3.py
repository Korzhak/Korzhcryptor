from string import (
    ascii_lowercase as al,
    ascii_uppercase as au,
    ascii_letters as a_let
)


class DateShift:
    def __init__(self, date_key: str = ""):
        """Date Shift Cipher
        :param date_key: date of your birthday. Example: 17/02/1998
        """
        self.date_key = self._parse_date(date_key)
        self.key_length = len(self.date_key)
        self.date_separated = [i for i in self.date_key]

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
        :return:
        """
        raw_text_int = self._get_index(raw_text)
        encode_text = ''
        i = 0
        for i in range(len(raw_text_int)):
            if raw_text[i].isalpha():
                value = (raw_text_int[i] + int(self.date_separated[i % self.key_length])) % len(al)
                encode_text += al[value]
            else:
                # add raw symbol to text
                encode_text += raw_text[i]

        return encode_text

    def decode(self, encode_text: str = None) -> str:
        """ Decoding text by Date Shift Cipher
        :param encode_text: text for decode
        :return:
        """
        encode_text_int = self._get_index(encode_text)
        decode_text = ''
        for i in range(len(encode_text_int)):
            if encode_text[i].isalpha():
                value = (encode_text_int[i] - int(self.date_separated[i % self.key_length])) % len(al)
                decode_text += al[value]
            else:
                # add raw symbol to text
                decode_text += encode_text[i]

        return decode_text
