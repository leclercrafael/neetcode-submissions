class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        frequencies = [None]* (len(nums) +1)
        for duo in seen.items():
            num = duo[0]
            freq = duo[1]
            if frequencies[freq] == None:
                frequencies[freq] = []
            frequencies[freq].append(num)
        final_order=[]
        for i in range(len(nums), -1, -1):
            if frequencies[i] != None:
                final_order += frequencies[i]

        return final_order[:k]