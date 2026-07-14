class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = dict()
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        if 0 not in seen:
            all=1
            for num in nums:
                all= all*num
            return [int(all/nums[i]) for i in range(len(nums))]

        if seen[0]>=2:
            return [0]*len(nums)
            
        if seen[0]==1:
            j=0
            for i in range(len(nums)):
                if nums[i]==0:
                    j=i
            all = 1
            for i in range(len(nums)):
                if i!=j:
                    all = all * nums[i]
            return [0 for i in range(j)] + [all] + [0 for i in range(j+1, len(nums))]
                
            

