class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        test = dict()

        for i in nums:
            if i in test :
                return True
            test[i]=1

        return False



        
        