leetcode 1662.Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1) #課本第2章的字串，有教 .split() 和 join()
        b = ''.join(word2) #單單join(word2)

        if a==b: return True # 兩字相同，就True相同
        else: return False # 否則相同