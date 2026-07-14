class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        current = {}
        max_f = 0
        out = 0
        l = 0

        for r in range(len(s)):

            current[s[r]] = current.get(s[r],0) + 1
            max_f = max(max_f, current[s[r]])

            while r-l+1 - max_f > k:
                current[s[l]]-=1
                l+=1

            out = max(out, r-l+1)

        return out
            

        
