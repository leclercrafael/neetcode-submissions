class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out=set(nums)
        nums[:len(out)] = sorted(list(out))
        return len(out)