def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        for n in nums:
            if n == 0:
                count+=1
                nums.pop(index)
            index+=1
        nums.extend([0]*count)
        print(nums)


moveZeroes([0,2,0,3,4,0,7])