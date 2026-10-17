class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                totalProduct *= n
        
        res = [0] * len(nums)
        if zeroCount > 1:
            return res
        for i in range(len(nums)):
            if zeroCount == 1:
                if nums[i] != 0:
                    res[i] = 0
                else:
                    res[i] = totalProduct
            else:
                res[i] = totalProduct // nums[i]
        return res
        
