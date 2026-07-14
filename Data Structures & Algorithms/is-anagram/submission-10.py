class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        if len(s)!= len(t):
            return False
        for i in range (len(s)):
            d[ord(s[i])] = d.get(ord(s[i]), 0) + 1
            d[ord(t[i])] = d.get(ord(t[i]), 0) - 1
        for value in d.values():
            if value != 0:
                return False
        return True