from collections import defaultdict
from typing import List

class Solution:

    def atMost(self, nums: List[int], k: int) -> int:

        left = 0
        count = 0
        freq = defaultdict(int)

        for right in range(len(nums)):

            # Add current element
            freq[nums[right]] += 1

            # Shrink window until distinct elements <= k
            while len(freq) > k:

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            # Count all valid subarrays ending at 'right'
            count += (right - left + 1)

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        return self.atMost(nums, k) - self.atMost(nums, k - 1)