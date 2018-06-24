def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) is 0:
        return 0
    mul = 0
    for x in range(len(array)):
        if x % 2 is 0:
            mul = mul + array[x]
    mul = mul * array[-1]
    return mul

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

