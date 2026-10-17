class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # getting initial total product and dividing
        res = [0] * len(nums)
        totalProduct = 1
        numberOfZero = 0
        for i in nums:
            if i != 0:
                totalProduct *= i
            else:
                numberOfZero += 1
        
        if numberOfZero > 1:
            return res
        
        for i in range(len(nums)):
            if numberOfZero == 1:
                if nums[i] == 0:
                    res[i] = totalProduct
                else:
                    res[i] = 0
            else:
                res[i] = totalProduct // nums[i]
        return res