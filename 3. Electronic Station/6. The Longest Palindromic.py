def longestPalindromic(word):
    max_polindrome = ''
    for i in range(len(word)):
        for j in range(len(word), 0, -1):
            current = word[i:j]
            reverse = current[::-1]
            if current == reverse and len(current) > len(max_polindrome):
                    max_polindrome = current 
    return max_polindrome

if __name__ == "__main__":
    assert longestPalindromic("artrartrt") == "rtrartr"
    assert longestPalindromic("abacada") == "aba"
    assert longestPalindromic("aaaa") == "aaaa"