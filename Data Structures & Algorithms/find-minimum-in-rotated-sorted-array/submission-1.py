class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        # print(f"length: {len(nums)} and mid: {len(nums)//2}")
        # print(f" mid_val: {nums[len(nums)//2]}")

        if len(nums) > 2:
            mid = len(nums) // 2 
            print(f"len: {len(nums)}, mid: {mid}, mid_val: {nums[mid]}, mid_val_+1: {nums[mid+1]}")
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            left_min = self.findMin(nums[:mid])
            
            right_min = self.findMin(nums[mid:])

            print(f"left min: {left_min}")
            print(f"right min: {right_min}")
            return min(left_min, right_min)
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        return nums[0]