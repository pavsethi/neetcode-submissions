class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #map char count to list of anagrams
        for s in strs:
            sortedS = ''.join(sorted(s))  
            res[sortedS].append(s)  #{'aet': ['eat']}
        return list(res.values())