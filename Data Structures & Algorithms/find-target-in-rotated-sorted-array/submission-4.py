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
                elif (nums[mid] > nums[hi]) and (target > nums[hi]):
                    hi = mid
                else:
                    hi = mid
            
            elif target > nums[mid]:

                if (nums[mid] < nums[lo]) and (target >= nums[lo]):
                    hi = mid 
                elif (nums[mid] < nums[lo]) and (target < nums[lo]):
                    lo = mid + 1
                else:
                    lo = mid + 1
        
        # [5, 1, 2, 3, 4], target = 1, low = 0, hi = 4
        # mid = 2, nums[mid] = 2
        # target < nums[mid]
        # lo = mid + 1 => lo = 3
        #

        return -1