class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validCloseToOpen = {"}": "{", "]": "[", ")": "("}

        for char in s:
            if char in validCloseToOpen:
                if stack and stack[-1] == validCloseToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0