class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
       #[ this is brute forcs approach in which we are not using division operator ]

        n=len(nums)
        ans=[1]*n
        for i in range(n):
            for j in range(n):
                if  i!=j:
                    ans[i]*=nums[j]
        return ans 
        ''' 
        n = len(nums)

        ans = [1] * n

        # Left product
        left = 1

        for i in range(n):
            ans[i] = ans[i] * left
            left = left * nums[i]

        # Right product
        right = 1

        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * right
            right = right * nums[i]

        return ans

        
        
