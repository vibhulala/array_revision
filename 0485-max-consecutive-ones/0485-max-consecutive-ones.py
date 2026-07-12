class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        for num in nums:
            if num==1:
                c+=1
            else:
                if c>m:
                    m=c
                c=0
        if c<m:
            return m
        else:
            return c 