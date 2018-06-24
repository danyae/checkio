def checkio(n, m):
    n_bin, m_bin = bin(n), bin(m)
    n_bin = list(reversed(list(n_bin)[2:]))
    m_bin = list(reversed(list(m_bin)[2:]))
    if len(m_bin) < len(n_bin):
        lst = ['0'] * (len(n_bin) - len(m_bin))
        m_bin.extend(lst)
    else:
        lst = ['0'] * (len(m_bin) - len(n_bin))
        n_bin.extend(lst)
    hamming_len = 0
    for i in range(len(m_bin)):
        if m_bin[i] != n_bin[i]:
            hamming_len += 1
    return hamming_len


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(16, 128) == 2, "4 example"
