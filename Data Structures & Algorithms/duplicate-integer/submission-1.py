class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for item in nums:
            count = 0
            for item2 in nums:
                if item == item2:
                    count += 1
            if count > 1:
                return True
        return False
        