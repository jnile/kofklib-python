import collections.abc

class Matrix(object):
    matrix = []
    
    #Constructor
    #
    # Defines a 2x2 Matrix
    def __init__(self, arr,):
        self.matrix = arr
        
        if type(arr[0]) is list:
            self.row = len(arr)
            self.columns = len(arr[0])
        else:
            self.matrix = [arr]
            self.row = 1
            self.columns = len(arr)
    
    @classmethod
    def blank_matrix(cls, rows, columns):
        temp_arr = [[0] * columns for i in range(rows)]
        return cls(temp_arr)
    
    
    
    #PrintMatrix
    #
    #Prints the matrix in terminal
    def printMatrix(self):
        print("Matrix:\n")
        
        for eachRow in self.matrix:
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
        return [[y for y in x] for x in self.matrix]
        