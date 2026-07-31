class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()# it is normal queue , in this we can delete from front and back 
        ans=[]# it will store maximum of every window 
        left=0 #left and 'r' is right 
        for right in range(len(nums)): # right window ko expand karenge :
            #remove indices which are out of the current window 
            while dq and dq[0]<left:
                dq.popleft()
            #remove all smaller elemenst from back 
            while dq and nums[dq[-1]]<nums[right]:
                dq.pop()
            #pusp currrent index
            dq.append(right)
            #first valid window 
            if right>=k-1:
                ans.append(nums[dq[0]])
                left+=1
        return ans


