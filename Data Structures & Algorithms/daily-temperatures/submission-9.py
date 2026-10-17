class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                prev_ind = stack.pop()
                result[prev_ind] = i - prev_ind
            stack.append(i)
        return result

            