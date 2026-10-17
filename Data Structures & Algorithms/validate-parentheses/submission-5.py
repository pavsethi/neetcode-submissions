class Solution:
    def isValid(self, s: str) -> bool:
        map_open_to_close = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for c in s:
            if c in map_open_to_close:
                stack.append(c)
            else:
                if len(stack) > 0 and map_open_to_close[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        