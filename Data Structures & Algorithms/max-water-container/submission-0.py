class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        max_a = 0

        while left < right:
            a = min(heights[left], heights[right]) * (right - left)

            if a > max_a:
                max_a = a
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_a