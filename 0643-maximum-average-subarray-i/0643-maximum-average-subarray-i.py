class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windows_sum=sum(nums[:k])
        max_sum=windows_sum
        for right in range(k,len(nums)):
            windows_sum+=nums[right]-nums[right-k]
            max_sum=max(max_sum,windows_sum)
        return max_sum/k