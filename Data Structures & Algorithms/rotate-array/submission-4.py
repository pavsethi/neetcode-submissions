class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        last = nums[(n-k):]
        first = nums[:(n-k)]
        print(last, first)
        nums[:] = last + first