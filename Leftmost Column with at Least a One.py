# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        
        c_row, c_col = 0, col - 1
        while c_row < row and c_col >= 0:
            if binaryMatrix.get(c_row, c_col) == 0:
                c_row += 1
            else:
                c_col -= 1
        if c_col == col - 1:
            return -1
        else:
            return c_col + 1
