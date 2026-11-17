class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) > 2:
            mid = len(nums) // 2 

            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            left_min = self.findMin(nums[:mid])
            
            right_min = self.findMin(nums[mid:])

            return min(left_min, right_min)

        elif len(nums) == 2:
            return min(nums[0], nums[1])

        return nums[0]