class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        if matrix[0][0] > target or matrix[len(matrix)-1][len(matrix[0])-1] < target:
            print("f2")
            return False

        l,r = 0,len(matrix)-1
        r1 = -1
        while l<=r:
            m = (l+r)//2
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[0])-1]:
                r1 = m
                break 
            elif target <  matrix[m][0]:
                r=m-1
            elif target >  matrix[m][len(matrix[0])-1]:
                l=m +1
        print(r1) 
        if r1 == -1:
            print("f2")
            return  False

        l,r=0, len(matrix[0])-1

        while l<=r:
            m = (l+r)//2

            if matrix[r1][m] == target:
                return True
            elif matrix[r1][m] > target :
                r = m-1
            elif matrix[r1][m] < target :
                l = m+1
        
        print("f3")
        return False
            
        

