class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        current = set()
        out=0

        for r in range(len(s)):
            while s[r] in current:
                current.remove(s[l])
                l+=1

            current.add(s[r])
            out = max(out, r-l+1)
        
        return out