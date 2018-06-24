def min(*args, key=lambda x: x):
    # key = kwargs.get("key", None)
    if len(args) == 1:
        new_args = args[0]
    else:
        new_args = args
    minimum = None
    started = False
    for x in new_args:
        if not started:
            started = True
            minimum = x
            continue
        if key(minimum) > key(x):
            minimum = x
    return minimum


def max(*args, key=lambda x: x):
    # key = kwargs.get("key", None)
    if len(args) == 1:
        new_args = args[0]
    else:
        new_args = args
    maximum = None
    started = False
    for x in new_args:
        if not started:
            started = True
            maximum = x
            continue
        if key(maximum) < key(x):
            maximum = x
    return maximum


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print(min(abs(i) for i in range(-10, 10)))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

