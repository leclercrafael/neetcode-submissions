class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]]
        max_right = [0]*len(height)
        m = height[0]
        n = height[-1]

        max_right[-1]=n
        for i in range(1,len(height)):
            m = max(m, height[i])
            max_left.append(m)

        for i in range(len(height)-1,-1,-1):
            n = max(n, height[i])
            max_right[i]=n

        out=0
        
        for i in range(len(height)):
            out += max(0, min(max_left[i], max_right[i])- height[i])

        return out


            