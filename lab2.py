class Palisade:
    @staticmethod
    def grouper(iterable, n):
        args = [iter(iterable)] * n
        return zip(*args)

    @staticmethod
    def encode(height: int = 1, raw_text: str = None) -> str:
        temp_height = height
        parent = []

        for i in range(height):
            parent.append(list())

        for i in raw_text:
            temp_height = (temp_height - 1) % height
            parent[temp_height].append(i)

        return ''.join([''.join(i) for i in parent])

    def decode(self, height: int = 1, encode_text: str = None) -> str:
        from math import ceil

        count_str = ceil(len(encode_text)/height)
        group = self.grouper(encode_text, count_str)
        parent = [''.join(i) for i in group]

        result = []
        for i in range(len(parent[0])):
            for j in range(len(parent)-1, -1, -1):
                result.append(parent[j][i])
        return ''.join(result)


p = Palisade()
h = 3
enc = p.encode(h, "Богдан Коржак  ")
dec = p.decode(h, enc)

print(enc + "\n" + dec)

