# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

try:
    nums = read_numbers()
    if not nums:
        # raise error if no numbers provided
        raise ValueError()
except:
    sys.exit("Number(s) is not valid")

nums.sort()
num_len = len(nums)
num_min = min(nums)
num_max = max(nums)
num_mean = sum(nums) / num_len

if num_len % 2 != 0:
    # odd number of items
    num_median = nums[int(num_len / 2)]
else:
    # even number of items
    num_median = (nums[int(num_len / 2 - 1)] + nums[int(num_len / 2)]) / 2

print("sorted nums: ", nums)
print(f"minimum: {num_min:.2f}")
print(f"maximum: {num_max:.2f}")
print(f"mean: {num_mean:.2f}")
print(f"median: {num_median:.2f}")