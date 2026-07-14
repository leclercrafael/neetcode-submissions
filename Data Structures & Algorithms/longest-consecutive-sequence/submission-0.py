class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        current = 0
        for x in nums:
            a = x
            current = 1
            if x-1 in nums:
                exit
            else:
                while a+1 in nums:
                    current +=1
                    a +=1
                best = max(current, best)
            
        return best
    




