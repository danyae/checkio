ROMAN_NUMS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000, '0': 0}

def reverse_roman(data):
    roman = data  # for debugger in VS Code
    number, previous = 0, '0'
    for l in reversed(roman):
        if ROMAN_NUMS[previous] > ROMAN_NUMS[l]:
            number -= ROMAN_NUMS[l]
        else:
            number += ROMAN_NUMS[l]
        previous = l
    return number


assert reverse_roman('VI') == 6
assert reverse_roman('LXXVI') == 76
assert reverse_roman('CDXCIX') == 499
assert reverse_roman('MMMDCCCLXXXVIII') == 3888