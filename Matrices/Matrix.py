class Matrix(object):
    matrix = []
    
    def __init__(self, rows, columns):
        self.matrix = [[0 for j in range(columns)] for i in range(rows)]   
            