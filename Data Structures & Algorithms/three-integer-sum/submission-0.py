class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        -4, -1, -1, 0, 1, 2
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:  #we alr reached positive side of sorted
                break
            if i > 0 and (nums[i] == nums[i - 1]):
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
