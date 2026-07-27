class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """this is brute force approach of this question
        it is bascially selecting and amking the subarrays one by one and maaking its product which
        is going to become the reason for TLE error
        c=0
        n=len(nums)
        for i in range(n):
            prd=1
            for j in range(i,n):
                prd*=nums[j]
                if prd>=k:
                    break
                c+=1
        return c
        """


# now we will move to better appraoch by making modificaion to the code
        if k<=1:
            return 0
        l = 0
        c = 0
        prd = 1
        for r in range(len(nums)):
            prd *= nums[r]
            while prd >= k:
                 prd /= nums[l]
                 l += 1
            c += r - l + 1
        return c
