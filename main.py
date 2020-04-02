import os
import random
import base64


class Randomizer:
    MAX_VALUE = 10**100

    @staticmethod
    def random_string(n: int = None):
        if n is None:
            n = random.randint(0, Randomizer.MAX_VALUE)
        return base64.b64encode(os.urandom(n)).decode()[:n]

    @staticmethod
    def random_number(only_pozitive: bool = False):
        if only_pozitive:
            return random.randint(0, Randomizer.MAX_VALUE)
        return random.randint(-Randomizer.MAX_VALUE, Randomizer.MAX_VALUE)

    @staticmethod
    def random_float(only_pozitive: bool = False):
        if only_pozitive:
            return random.random()
        return random.random() * (-1 * random.random() > 0.5)

    @staticmethod
    def random_list(t: type, n: int = None):
        TYPE_MAP = {
            int: Randomizer.random_number,
            str: Randomizer.random_string,
            float: Randomizer.random_float,
        }
        try:
            method = TYPE_MAP[t]
        except KeyError:
            raise TypeError
        if n is None:
            n = random.randint(0, Randomizer.MAX_VALUE)
        return [method() for _ in range(n)]
