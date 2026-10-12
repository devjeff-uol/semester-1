# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

nums = read_numbers()
if not nums:
    sys.exit("Error: no numbers provided")

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

print(f"Minimum = {num_min:.1f}")
print(f"Maximum = {num_max:.1f}")
print(f"Mean = {num_mean:.1f}")
print(f"Median = {num_median:.2f}")