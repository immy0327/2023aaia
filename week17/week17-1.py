2610

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [ [ nums[0] ] ] # 把最前面、最小的數字，放在兩層方括號裡
        repeat = 0
        N = len(nums)
        for i in range(1,N):
            if nums[i] == nums[i-1]:
                repeat += 1
                if len(ans)<=repeat:
                   ans.append( [] )
            else:
                repeat = 0
            ans[repeat].append( nums[i] )
        return ans 