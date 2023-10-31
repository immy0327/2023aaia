# Find tje difference week08-6
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {} 
        for c in s:
            if c in d:
               d[c] = d[c] + 1
            else:
               d[c] = 1
        print(d)

        for c in t:
            if c not in d: # 不在字典, 字母出現次數統計結果
                return c
            if  d[c]<=0: # 不夠
                return c # 找到多出來的字母
            else:
               d[c] = d[c] - 1
        return ""