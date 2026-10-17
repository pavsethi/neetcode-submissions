class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for n in range(len(numbers)):
            diff = target - numbers[n]
            if diff in seen:
                return [seen[diff], n + 1]
            seen[numbers[n]] = n + 1
        return