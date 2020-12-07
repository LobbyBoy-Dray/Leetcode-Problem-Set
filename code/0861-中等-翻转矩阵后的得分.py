def matrixScore(A):
    # 0. 
    if A == []:
        return 0
    # 1. 
    for row_idx in range(len(A)):
        if A[row_idx][0] != 1:
            A[row_idx] = [1-i for i in A[row_idx]]
    # 2. 
    num_row = len(A)
    num_col = len(A[0])
    res     = 2**(num_col-1)*num_row
    for i in range(1, num_col):
        tmp = sum([row[i] for row in A])
        if tmp <= num_row//2:
            res += 2**(num_col-1-i) * (num_row-tmp)
        else:
            res += 2**(num_col-1-i) * tmp
    return res