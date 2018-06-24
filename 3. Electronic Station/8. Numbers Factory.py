#get all multipliers. If len(multiplier) > 1, we can't multiply it's digits
def multipliers(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
       ans.append(n)
    for num in ans:
        if len(str(num)) > 1:
            return [0]
    return ans

def digits_from(delims, n):
    mul_list = delims[:]
    counter = 0
    while(counter + 1 < len(mul_list)):
        replacement_num = mul_list[counter] * mul_list[counter + 1]
        if(replacement_num < 10):
            mul_list[counter] = replacement_num
            del mul_list[counter + 1]
        else:
            counter += 1
    number_str = "".join(str(x) for x in sorted(mul_list))
    if '1' in number_str or '0' in number_str:
        return 0
    else:
        return int(number_str)

def checkio(n):
    delims = multipliers(n)
    if len(delims) == 1:
        return 0
    answer = digits_from(delims, n)
    answer2 = digits_from(sorted(delims, reverse=True), n)
    if answer <= answer2 and answer != 0:
        return answer
    elif answer2 < answer and answer2 != 0:
        return answer2
    else:
        return 0
    
    

if __name__ == '__main__':
    print(multipliers(12))
    print(checkio(12))
    print(checkio(20))
    assert checkio(20) == 45
    assert checkio(21) == 37
    assert checkio(17) == 0
    assert checkio(33) == 0
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
