class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointerS = pointerT = 0 

        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
                pointerT += 1
            else:
                pointerS += 1
        
        return len(t) - pointerT

