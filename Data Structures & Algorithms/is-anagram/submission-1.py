class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        out1={}
        out2={}

        for i in s:
            if i in out1:
                out1[i]+=1
            else:
                out1[i]=1

        for i in t:
            if i in out2:
                out2[i]+=1
            else:
                out2[i]=1

        return out1==out2
        