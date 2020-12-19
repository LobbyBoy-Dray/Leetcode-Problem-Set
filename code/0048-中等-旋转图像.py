def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)//2):
        matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]
    
    for row in range(len(matrix)):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]