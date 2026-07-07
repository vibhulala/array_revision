class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        this is basically better solution approach 
        '''
        #  n = len(nums)
        # # Counters for each color
        # cnt1 = 0  # number of 0s
        # cnt2 = 0  # number of 1s
        # cnt3 = 0  # number of 2s

        # # First pass – count frequencies
        # for i in range(0, n):
        #     if nums[i] == 0:
        #         cnt1 += 1
        #     elif nums[i] == 1:
        #         cnt2 += 1
        #     else:
        #         cnt3 += 1

        # # Second pass – overwrite array based on counts
        # for i in range(0, cnt1):
        #     nums[i] = 0
        # for i in range(cnt1, cnt1 + cnt2):
        #     nums[i] = 1
        # for i in range(cnt1 + cnt2, cnt1 + cnt2 + cnt3):
        #     nums[i] = 2

        ''' now we will move to optimal solution  i.e: THREE POINTERS'''
        l=0#low
        m=0#mid
        h=len(nums)-1#high 
        while m<=h:# area of unprocessed elements
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                m +=1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1 

''' 0_ _ _ low-1---> 0's
    low_ _ _ mid-1--->1's
    mid_ _  _high---->unknown/unprocessed elements (basically here only we are definning our looping condition)
    high+1_ _ _ _end---->2's
    '''