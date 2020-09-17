MAGIC = 'ADFGVX'


class ADFGVX:
    @staticmethod
    def encode(message, secret_alphabet1, keyword):
        key = []
        for c in keyword:
            if c not in key:
                key.append(c)

        n = len(key)
        k = sorted(range(n), key=lambda i: key[i])

        s = []
        for c in message.lower():
            if c.isalpha() or c.isdigit():
                row, col = divmod(secret_alphabet1.index(c), 6)
                s += [MAGIC[row], MAGIC[col]]

        return ''.join(s[j] for i in k for j in range(i, len(s), n))

    @staticmethod
    def decode(message, secret_alphabet1, keyword):
        key = []
        for c in keyword:
            if c not in key: key.append(c)

        n = len(key)
        k = sorted(range(n), key=lambda i: key[i])

        m = len(message)
        x = [j for i in k for j in range(i, m, n)]

        y = ['']*m
        for i, c in zip(x, message): y[i] = c

        s = []
        for i in range(0, m, 2):
            row, col = y[i:i+2]
            s.append(secret_alphabet1[6 * MAGIC.index(row) + MAGIC.index(col)])
        return ''.join(s)


a = ADFGVX()

print(a.encode("Bohdan Korzhak", 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g', 'cipher'))
print(a.decode("FAGFGAGXDXVXDDAXFXDDDADDDV", 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g', 'cipher'))

