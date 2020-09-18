"""
Name: Lab #5
Author: Bohdan Korzhak
Group: AKSm-19-1
Description: Encryptor by Shuffle Cipher
"""

import random


class ShuffleCipher:
    @staticmethod
    def encode(s, key):
        random.seed(key)
        ln = len(s)
        keys = random.sample(range(ln), ln)
        out = ''
        for i in keys:
            out += s[i]
        return out

    @staticmethod
    def decode(s, key):
        random.seed(key)
        ln = len(s)
        keys = random.sample(range(ln), ln)
        out = [' ' for _ in range(ln)]
        for i, j in zip(keys, s):
            out[i] = j
        return ''.join(out)


sc = ShuffleCipher()
s1 = sc.encode('Example encrypted string', 5)
print('crypt:\n' + s1)
print('encrypt:\n' + sc.decode(s1, 5))
