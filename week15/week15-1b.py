# leetcode 1913
# 把最大的2個相乘 - 最小的兩個相乘
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        N = len(nums)

        return nums[N-1]*nums[N-2] - nums[0]*nums[1]