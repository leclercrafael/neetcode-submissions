class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for x in nums:
            if x in frequencies:
                frequencies[x]+=1
            else:
                frequencies[x]=1

        count = sorted(list(frequencies.values()))
        out=[]
        for i in range(1,k+1):
            to_find = count[len(count)-i]
            for x in frequencies.keys():
                if frequencies[x]==to_find:
                    out.append(x)
                    del frequencies[x]
                    break
        return out