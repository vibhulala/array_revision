class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        peak=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                peak+=1
        return peak<=1