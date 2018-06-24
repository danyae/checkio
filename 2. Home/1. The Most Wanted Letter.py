def checkio(text):
    chars = map(chr, range(ord('a'), ord('z')+1))
    letters = dict((el, 0) for el in chars)
    text = text.lower()
    for l in text:
        if l not in letters:
            continue
        letters[l] += 1

    maxkey = 'a'
    maxvalue = 0
    for x in letters:
        if letters[x] > maxvalue:
            maxvalue = letters[x]
            maxkey = x
    return maxkey

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

