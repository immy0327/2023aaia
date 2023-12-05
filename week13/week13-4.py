# Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 # 迴圈在前面 ans=0

        while n>0: # 要把 n 刪光光
            ans += n%2 # 剝下來的皮
            n = n //2 # n剝完就變小

        return ans # 迴圈後面 ans拿來用
        