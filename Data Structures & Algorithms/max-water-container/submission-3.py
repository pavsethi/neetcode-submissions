class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width
            maxArea = max(area, maxArea)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea
