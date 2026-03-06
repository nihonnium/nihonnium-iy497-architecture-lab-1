def sum_to_n (n:int) -> int:
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def count_positives(nums:list[int]) -> int:
    count = 0
    for x in nums:
        if x > 0:
            count += 1
    return count


def  max_value(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Empty list")
    current_max = nums[0]
    for x in nums[1:]:
        if x > current_max:
            current_max = x
    return current_max


#Test:
print (sum_to_n(3))
print (count_positives([-1,2,-3,4,5]))
print (max_value([2,4,7,9,-2]))