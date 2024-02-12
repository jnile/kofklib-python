class Matrix(object):
    matrix = []
    
    
    def __init__(self, rows, columns):
        self.matrix = [[0 for j in range(columns)] for i in range(rows)]
        self.rows = rows  
        self.columns = columns  
    
    def printMatrix(self):
        print("Matrix:\n")
        
        for eachRow in self.matrix:
            row = ""
            for eachCol in eachRow:
                row += str(eachCol) + " "
            
            row += "\n"
            print(row)
            
        print("\n")