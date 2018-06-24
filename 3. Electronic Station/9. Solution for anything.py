import re
import math


class checkio():
    def __init__(self, smth):
        self.smth = smth

    def __call__(self, smth):
        self.smth = smth

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __le__(self, other):
        return True

if __name__ == '__main__':
    assert checkio({}) != []  # True
    assert checkio('Hello') < 'World'  # True
    assert checkio(80) > 81  # True
    assert checkio(re) >= re  # True
    assert checkio(re) <= math  # True
    assert checkio(5) == ord  # True
