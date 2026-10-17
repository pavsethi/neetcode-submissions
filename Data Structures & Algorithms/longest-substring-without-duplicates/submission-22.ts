class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s: string): number {
        let seen = new Set<string>();
        let l: number = 0
        let maxLen = 0
        for (let i = 0; i < s.length; i++){
            while (seen.has(s[i])){
                seen.delete(s[l]);
                l++;
            }
            seen.add(s[i])
            maxLen = Math.max(maxLen, seen.size);
        }
        return maxLen
    }
}
