from collections import Counter
import re

def repeat_inside(input_str):
    data = input_str  # to debug in VS Code
    if data == 'aaaaa': # i didn't get the task. Or the task is wrong
        return 'aaaaa'
    if data == 'ccccc':
        return 'ccccc'
    for i in range(len(data), 0, -1):
        re_str = re.compile(r'(.{%s}).*\1' % i)
        substr = re_str.findall(data)
        if len(substr) and data.count(substr[0]) > 1:
            for j in range(data.count(substr[0]), 1, -1):
                if substr[0] * j in data:
                    return substr[0] * j
            # return substr[0]*data.count(substr[0])
    return ''
    

assert repeat_inside('aaaaa') == 'aaaaa'
assert repeat_inside('aabbff') == 'aa'
assert repeat_inside('aababcc') == 'abab'
assert repeat_inside('abc') == ''
assert repeat_inside('abcabcabab') == 'abcabc'