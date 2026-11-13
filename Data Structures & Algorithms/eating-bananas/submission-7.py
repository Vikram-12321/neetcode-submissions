class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)  # safe lower bound is 1

        while l <= r:
            mid = (l + r) // 2
            # total_time = sum( (p + mid - 1) // mid  for p in piles)  # ceil(p/mid)
            total_time = sum( math.ceil(p / mid)  for p in piles) 

            if total_time <= h:
                r = mid - 1      # mid works; try smaller
            else:
                l = mid + 1      # mid too slow; need bigger

        return l
