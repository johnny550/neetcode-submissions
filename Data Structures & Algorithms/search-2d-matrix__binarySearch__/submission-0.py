class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerp0, outerp1 = 0, len(matrix) - 1
        
        while outerp0 <= outerp1:
            list_div=abs((outerp0 + outerp1) // 2)
            if matrix[0] and matrix[list_div][0]>target:
                # check in list on the left
                outerp1 = list_div - 1
                # continue
            elif matrix[0] and matrix[list_div][0]<target:
                # check in list on the right
                outerp0= list_div + 1 
                # continue
            elif matrix[0] and matrix[list_div][0]==target:
                return True
                
            if matrix[list_div] != []:
                innerp0, innerp1 = 0, len(matrix[list_div]) - 1
                while innerp0 <= innerp1:
                    inner_div=abs((innerp0 + innerp1) // 2)
                    if matrix[list_div][inner_div]==target:
                        return True
                    elif matrix[list_div][inner_div]<target:
                        # move right
                        innerp0 = inner_div + 1
                        continue
                    else:
                        # move left
                        innerp1 = inner_div - 1
                        continue
                # continue
        return False