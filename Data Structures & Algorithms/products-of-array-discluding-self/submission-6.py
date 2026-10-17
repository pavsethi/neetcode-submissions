class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        totalProduct = 1
        for n in nums:
            if n == 0:
                zeroCount += 1
            else:
                totalProduct *= n
        if zeroCount > 1:
            return [0] * len(nums)
        
        ret = [0] * len(nums)
        for n in range(len(nums)):
            if zeroCount == 1:
                if nums[n] == 0:
                    ret[n] = totalProduct
                else:
                    ret[n] = 0
            else:
                ret[n] = totalProduct // nums[n]
        return ret
