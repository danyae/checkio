from functools import reduce


def checkio(number):
    nums = [x for x in str(number) if x != '0']
    mult = reduce((lambda x, y: int(x) * int(y)), nums)
    return int(mult)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

