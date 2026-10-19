class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        1, 2, 0, 0, 5, 0
        1, 2, 5, 0, 0, 0
        while r < len(nums) - 1:
            if nums[l] != 0:
                l += 1
                r += 1
            
            while r < len(nums) - 1 and nums[r] == 0:
                r += 1
            if r != l:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp