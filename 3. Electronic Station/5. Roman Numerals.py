def checkio(num):
    rome_str = ''
    num_of_digits = [0, 0, 0, 0] #thousands, hundreds, dozens, units
    for i in range(3, -1, -1):
        num_of_digits[i] = num % 10
        num = num // 10

    rome_str += num_of_digits[0] * 'M'
    if num_of_digits[1] == 9:
        rome_str += 'CM'
    elif num_of_digits[1] > 4:
        rome_str += 'D' + (num_of_digits[1] - 5) * 'C'
    elif num_of_digits[1] == 4:
        rome_str += 'CD'
    else:
        rome_str += num_of_digits[1] * 'C'
    
    if num_of_digits[2] == 9:
        rome_str += 'XC'
    elif num_of_digits[2] > 4:
        rome_str += 'L' + (num_of_digits[2] - 5) * 'X'
    elif num_of_digits[2] == 4:
        rome_str += 'XL'
    else:
        rome_str += num_of_digits[2] * 'X'
    
    if num_of_digits[3] == 9:
        rome_str += 'IX'
    elif num_of_digits[3] > 4:
        rome_str += 'V' + (num_of_digits[3] - 5) * 'I'
    elif num_of_digits[3] == 4:
        rome_str += 'IV'
    else:
        rome_str += num_of_digits[3] * 'I'
    return rome_str

def checkio2(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result

if __name__ == '__main__':    
    # assert checkio(6) == 'VI'
    # assert checkio(76) == 'LXXVI'
    # assert checkio(13) == 'XIII'
    # assert checkio(44) == 'XLIV'
    assert checkio2(3999) == 'MMMCMXCIX'
    assert checkio(1000) == 'M'