from typing import List

class Matrix(object):
    _matrix = []
    
    #Constructor
    #
    # Defines a 2x2 Matrix
    def __init__(self, arr: List):
        self._matrix = arr
        
        if type(arr[0]) is list:
            self._rows = len(arr)
            self._columns = len(arr[0])
        else:
            self._matrix = [arr]
            self._rows = 1
            self._columns = len(arr)
    
    @classmethod
    def blank_matrix(cls, rows, columns):
        temp_arr = [[0] * columns for i in range(rows)]
        return cls(temp_arr)
    
    
    
    #PrintMatrix
    #
    #Prints the matrix in terminal
    def printMatrix(self):
        print("Matrix:\n")
        
        for eachRow in self._matrix:
            row = ""
            
            for eachCol in eachRow:
                row += str(eachCol) + " "
            
            row += "\n"
            print(row)
            
        print("\n")
    
    #getMatrix
    #
    # Return the matrix as an array
    def getMatrix(self):
        return [[y for y in x] for x in self._matrix]
    
    def getRows(self):
        return self._rows
    
    def getCols(self):
        return self._columns
    
    #Returns the value at x,y in the matrix
    # 
    # x - int - index of the row
    # y - int - index of the column
    def getValue(self,x,y):
        return self._matrix[x][y]
    
    # Performs the dot product of matrices A.B
    #
    # matB - Matrix - Matrix B which has the same number of rows as the number of columns as Matrix A (calling matrix)
    def dotProduct(self, matB):
        if self._columns != matB.getRows():
            raise Exception(f"Number of Rows and the Number of Columns do not match.\n Called Matrix A has {self._columns}.\n Input Matrix B has {matB.getRows()}.")
        temp_matrix = []
        
        for i in range(self._rows):
            temp_row = []
            for j in range(matB.getCols()):
                total_sum = 0
                
                for n in range(self._columns):
                    total_sum += self.getValue(i,n)*matB.getValue(n,j)
                    
                temp_row.append(total_sum)
            temp_matrix.append(temp_row)
        
        return Matrix(temp_matrix)