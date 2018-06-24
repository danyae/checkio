def checkio(data):
    if len(data) < 10:
        return False
    numbers = 0
    small_letters = 0
    big_letters = 0
    for x in data:
        if x.isnumeric():
            numbers += 1
        if x.islower():
            small_letters += 1
        if x.isupper():
            big_letters += 1
    if numbers == 0:
        return False
    if small_letters == 0:
        return False
    if big_letters == 0:
        return False
    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

