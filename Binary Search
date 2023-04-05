comparisons = 0
recursions = 0

def binary_search(nums, target, lower, upper):
    global comparisons
    global recursions
    comparisons += 1
    recursions += 1
    index = (lower + upper) // 2

    if target == nums[index]:
        return index
    elif (lower == upper):
        return -1

    if target < nums[index]:
        comparisons += 1
        return binary_search(nums, target, lower, index - 1)

    else:
        comparisons += 1
        return binary_search(nums, target, index + 1, upper)


if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]

    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
