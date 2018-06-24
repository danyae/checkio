def checkio(expression):
    closing_br = {'(': ')', '[': ']', '{': '}'}
    opening_br = {')': '(', ']': '[', '}': '{'}
    curr_brackets = []
    expected_brackets = []
    error = False
    for x in expression:
        if x in closing_br:
            curr_brackets.append(x)
            expected_brackets.insert(0, closing_br[x])
        if x in opening_br:
            try:
                if expected_brackets[0] == x:
                    del curr_brackets[-1]
                    del expected_brackets[0]
                else:
                    return False
            except IndexError:
                return False

    if len(expected_brackets) > 0:
        return False
    return True

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False

