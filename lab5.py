import random


class ShuffleCipher:
    @staticmethod
    def crypto(s, key):
        random.seed(key)
        ln = len(s)
        keys = random.sample(range(ln), ln)
        out = ''
        for i in keys:
            out += s[i]
        return out

    @staticmethod
    def encrypt(s, key):
        random.seed(key)
        ln = len(s)
        keys = random.sample(range(ln), ln)
        out = [' ' for _ in range(ln)]
        for i, j in zip(keys, s):
            out[i] = j
        return ''.join(out)


sc = ShuffleCipher()
s1 = sc.crypto('Example encrypted string', 5)
print('crypt:\n' + s1)
print('encrypt:\n' + sc.encrypt(s1, 5))
