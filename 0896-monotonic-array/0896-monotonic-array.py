class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)
        inc=False
        dec=False 
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                inc=True
            if nums[i]>nums[i+1]:
                dec=True
        if inc==True and dec==True :
            return False
        return True