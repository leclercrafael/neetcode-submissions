class Solution:
    def trap(self, height: List[int]) -> int:
        seen = dict()
        for i in range(len(height)):
            seen[i]=[False, None, None]
            h = height[i]
            for j in range(len(height)):
                if j<i and height[j]>height[i]:
                    if seen[i][1] == None:
                        seen[i][1] = height[j]
                    else:
                        seen[i][1]= max(seen[i][1], height[j])
                if i<j and height[j]>height[i]:
                    if seen[i][2] == None :
                        seen[i][2] = height[j]
                    else:
                        seen[i][2]= max(seen[i][2], height[j])
                    if seen[i][1] != None:
                        seen[i][0]=True
        out=0
        for item in seen.items():
            print(item[0])
            if item[1][0]==True:
                out+=min(item[1][1], item[1][2])-height[int(item[0])]

        return out
            