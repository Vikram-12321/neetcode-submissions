class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        nums.sort()
        def dfs(start, total):
            if total == target:
                res.append(path[:])
                return
            
            for j in range(start, len(nums)):
                if total + nums[j] > target:
                    break

                path.append(nums[j])
                dfs(j, total + nums[j])
                path.pop()
                
        dfs(0, 0)
        return res