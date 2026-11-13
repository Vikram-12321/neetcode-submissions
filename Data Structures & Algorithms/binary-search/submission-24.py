class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        if n == 0: return -1

        half = n //  2
        

        if nums[half] == target: 
            return half 
        
        elif n > 1:
            from_left = False

            if nums[half] > target:   # nums[1] = 5 > 2 - YES
                to_return = self.search(nums[:half], target)  # 2: nums = [2]
                from_left = True

            elif nums[half] < target:   # nums[3] = 5 < 9 - Yes
                to_return = self.search(nums[half+1:], target) # Last 3 items, 2: nums = [5, 9, 12]


            if to_return == -1:
                return -1
                
            else:
                if from_left:
                    return to_return
                
                to_return += half + 1
                return to_return

        return -1
    