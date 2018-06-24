def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if line == '':
        return 0
    longest = 1
    current = 1
    previous = ''
    for x in line:
        if x == previous:
            current += 1
            if longest < current:
                longest = current
        else:
            previous = x
            if longest < current:
                longest = current
            current = 1
    return longest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('aavvrwwwrggg') == 3, "Second"
    print(long_repeat(''))
    print(long_repeat('aa'))
    print('"Run" is good. How is "Check"?')

