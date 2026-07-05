class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for key,value in enumerate(nums):
            req=target-value
            if req in hash_map:
                return [hash_map[req],key]
            hash_map[value]=key

