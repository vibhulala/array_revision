class Solution:
    def thirdMax(self, nums):

        first = float('-inf')
        second = float('-inf')
        third =float('-inf')

        for num in nums:

            # Case 0
            # Duplicate hai?
            # continue
            if num==first or num==second or num==third :#"First I ignore duplicates, then I update first, second and third."
                continue

            # Case 1
            # Agar first se bada hai

                # third = ?
                # second = ?
                # first = ?
            if num >first:
                third=second 
                second=first
                first=num 

            # Case 2
            # Agar second se bada hai

                # third = ?
                # second = ?
            elif num >second :
                third =second 
                second =num 
            # Case 3
            # Agar third se bada hai
            elif num > third:
                third = num

        # Yahan decide karna hai
        if third==float('-inf'):
            return first 
        return third

        # Agar third exist hi nahi karta
        # return ?

        # Warna
        # return ?