class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_dict(string):
            d = dict()
            for letter in string:
                if letter in d:
                    d[letter]+=1
                else:
                    d[letter]=1
            return d
        return create_dict(s)==create_dict(t)