# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array)==0 or len(array[0])==0 or target < array[0][0] or target > array[-1][-1]:
            return False

        row = 0    #end_row
        column = len(array[0]) - 1
        while row < len(array) and column >= 0:
            if array[row][column] == target:
                return True
            elif array[row][column] > target:
                column -= 1
            else:
                row += 1
        return False
                        
                
solution = Solution()
result = solution.Find(7,[[1,2,3],[4,5,7],[8,9,11]])
print(result)
