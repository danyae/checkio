import re


def checkio(matrix):
    pattern = r'.*(?:(\d)\1{3})'
    prog = re.compile(pattern)
    dimension = len(matrix)
    for i in range(dimension):
        row = ''.join([str(x) for x in matrix[i]])
        if prog.match(row):
            return True
        column = ''.join([str(row[i]) for row in matrix])
        if prog.match(column):
            return True
    diagonals = get_diagonals(matrix)
    for x in diagonals:
        if prog.match(x):
            return True
    return False


def get_diagonals(matrix):
    h, w = len(matrix), len(matrix[0])
    diagonals = [[matrix[h - p + q - 1][q]
                 for q in range(max(p-h+1, 0), min(p+1, w))]
                 for p in range(h + w - 1)]
    antidiagonals = [[matrix[p - q][q]
                     for q in range(max(p - h + 1, 0), min(p+1, w))]
                     for p in range(h + w - 1)]
    diagonals.extend(antidiagonals)
    diagonals = [x for x in diagonals if len(x) >= 4]
    for i in range(len(diagonals)):
        diagonals[i] = ''.join(str(x) for x in diagonals[i])
    return diagonals

if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) is True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) is False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) is True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
        ]) is True
    