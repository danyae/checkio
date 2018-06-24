def checkio(nums):
    if len(nums) == 0:
        return 0
    else: return nums[0] + checkio(nums[1:])

if __name__ == '__main__':
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12