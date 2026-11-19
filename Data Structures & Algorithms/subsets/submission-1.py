class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:     
        res, path = [], []

        def dfs(i):
            if len(nums) == i:
                res.append(path[:]) ## append new copy
                return
            
            path.append(nums[i]) ## choose 1
            dfs(i+1)
            path.pop()
            dfs(i+1) ## Don't choose 1

        dfs(0)
        return res




