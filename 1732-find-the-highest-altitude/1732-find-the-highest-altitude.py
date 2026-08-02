class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        max_alt=0
        for chg in gain:
            alt+=chg
            max_alt=max(alt,max_alt)
        return max_alt 