class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        best_area = (r-l)*min(heights[r], heights[l])
        while l<r:
            if heights[l]<=heights[r]:
                l+=1
                if (r-l)*min(heights[l], heights[r])>best_area:
                    best_area = (r-l)*min(heights[l], heights[r])
            else:
                r-=1
                if (r-l)*min(heights[l], heights[r])>best_area:
                    best_area = (r-l)*min(heights[l], heights[r])
        return best_area


