class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if len(nums) == 1 and target == nums[0]:
            return 0

        while lo < hi:
            mid = (hi + lo) // 2

            if target == nums[lo]:
                return lo
            if target == nums[hi]:
                return hi
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                if (nums[mid] > nums[hi]) and (target <= nums[hi]):
                    lo = mid + 1
                else:
                    hi = mid
            
            else:
                if (nums[mid] < nums[lo]) and (target >= nums[lo]):
                    hi = mid 
                else:
                    lo = mid + 1
        
        return -1