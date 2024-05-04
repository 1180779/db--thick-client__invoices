from random import randint

class AccountGen(object):
    def __init__(self, len = 12):
        if not isinstance(len, int):
            raise TypeError
        elif len < 1:
            raise ValueError
        self.len = len

    def Generate(self):
        res = '\''
        for i in range(1, self.len):
            res = res + chr(ord('0') + randint(0, 9))
        return res + '\''