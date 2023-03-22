from utils.test_program_output import test_output


def two_sum_sorted(nums, target):
    nums = sorted(nums)
    begin = 0
    end = len(nums) - 1

    while begin < end:
        check = nums[begin] + nums[end]
        if check == target:
            return [begin, end]
        elif check < target:
            begin += 1
        elif check > target:
            end -= 1
    return -1


def two_sum(nums, target):
    pair = {}

    for i in range(len(nums)):
        if target - nums[i] in pair:
            return [pair[target - nums[i]], i]
        else:
            pair[nums[i]] = i
    return -1


test_data = [([[2, 7, 11, 15], 9], [0, 1]),
             ([[3, 2, 4], 6], [1, 2]), ([[3, 3], 6], [0, 1])]

if __name__ == "__main__":
    test_output(test_data, two_sum, True, 2)
