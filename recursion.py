numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]

def recursive_sum(nums):
    total = 0
    for num in nums:
        if type(num) is int:
            total += num
        else:
            total += recursive_sum(num)
    return total