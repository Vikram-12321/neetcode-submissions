class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j and (nums[i]+nums[j] == target):
                    sums[i+j] = [j,i]

        return sums[min(sums)]
