class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
        # target=11

        d, u = 0, len(matrix) - 1 

        while d <= u:
            mid_du = (d + u) // 2 
            
            if matrix[mid_du][0] == target: 
                return True 

            elif matrix[mid_du][0] > target: 
                u = mid_du - 1
            else:
                d = mid_du + 1 

        l, r = 0, len(matrix[u]) - 1 

        while l <= r:
            mid_lr = (l + r) // 2 

            if matrix[u][mid_lr] == target: 
                return True
            elif matrix[u][mid_lr] > target:
                r = mid_lr - 1
            else:
                l = mid_lr + 1

        return False

        
