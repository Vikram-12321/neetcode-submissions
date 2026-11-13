class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
        # target=11

        d, u = 0, len(matrix) - 1 # d = 0, u = 2

        while d <= u:
            mid_du = (d + u) // 2 # mid_du = 1, 2: (3//2) = 1
            
            if matrix[mid_du][0] == target: 
                return True 

            elif matrix[mid_du][0] > target: # matrix[1][0] = 10 > target = False
                u = mid_du - 1
            else:
                d = mid_du + 1 # d = 2

        row_target = matrix[u]  # [10,11,16,20]

        l, r = 0, len(row_target) - 1 # l = 0, r = 3

        while l <= r:
            mid_lr = (l + r) // 2 # 1: mid_lr = 1

            if row_target[mid_lr] == target: # 11 = 11 
                return True
            elif row_target[mid_lr] > target:
                r = mid_lr - 1
            else:
                l = mid_lr + 1

        return False

        
