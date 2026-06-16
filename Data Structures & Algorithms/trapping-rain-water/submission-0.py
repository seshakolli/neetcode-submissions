class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res=0
        i,j= 0, len(height)-1
        MaxL, MaxR = height[i], height[j]
        while i<j:
            if MaxL < MaxR:
                i+=1
                MaxL= max(MaxL, height[i])
                res+= MaxL- height[i]
            else:
                j-=1
                MaxR= max(MaxR, height[j])
                res+= MaxR - height[j]
        return res
