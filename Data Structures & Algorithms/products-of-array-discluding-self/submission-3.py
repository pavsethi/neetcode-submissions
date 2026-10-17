class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0
        for n in nums:
            if n != 0:
                totalProduct *= n
            else:
                zeroCount += 1
        
        res = [0] * len(nums)
        if zeroCount > 1:
            return res
        
        for n in range(len(nums)):
            if zeroCount == 1:
                if nums[n] == 0:
                    res[n] = totalProduct
                else:
                    res[n] = 0
            else:
                res[n] = totalProduct // nums[n]
        return res