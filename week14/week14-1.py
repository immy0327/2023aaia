leetcode 1464.Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0 #用來放答案的變數

        N = len(nums) #nums這個陣列 list有幾個數
        for i in range( N ): #左手i
            for j in range( i+1, N): #右手j
                ans = max( ans,  (nums[i]-1)*(nums[j]-1)) # 照題目去找相乘的最大值
        return ans