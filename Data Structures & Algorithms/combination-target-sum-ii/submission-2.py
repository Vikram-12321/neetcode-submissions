class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        candidates.sort()

        def dfs(start, total):
            if total == target:
                res.append(path[:])
                return
            
            for j in range(start, len(candidates)):

                if total + candidates[j] > target:
                    break

                if j > start and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])

                dfs(j+1, total + candidates[j])
                path.pop()
                
        dfs(0, 0)
        return res
